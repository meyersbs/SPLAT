#!/usr/bin/env python3

##### PYTHON IMPORTS ###################################################################################################
import os.path, sys, json

##### SPLAT IMPORTS ####################################################################################################
from splat.gramminators.FullNGramminator import FullNGramminator
from splat.parsers.TreeStringParser import TreeStringParser
from splat.sentenizers.CleanSentenizer import CleanSentenizer
from splat.taggers.NLTKPOSTagger import NLTKPOSTagger
from splat.tokenizers.RawTokenizer import RawTokenizer
from splat.tokenizers.CleanTokenizer import CleanTokenizer
import splat.Util as Util
import splat.complexity.Util as cUtil

########################################################################################################################
##### INFORMATION ######################################################################################################
### @PROJECT_NAME:		SPLAT: Speech Processing and Linguistic Analysis Tool										 ###
### @VERSION_NUMBER:																								 ###
### @PROJECT_SITE:		github.com/meyersbs/SPLAT																     ###
### @AUTHOR_NAME:		Benjamin S. Meyers																			 ###
### @CONTACT_EMAIL:		ben@splat-library.org																		 ###
### @LICENSE_TYPE:		MIT																							 ###
########################################################################################################################
########################################################################################################################

class SPLAT:
    """
    A SPLAT is a selection of text. It can be a single word, a paragraph, or even a whole novel!
    The SPLAT object makes it super simple to extract features from a selection of text.
    """
    # Basic Feature Variables
    __wordcount, __unique_wordcount, __sentcount, __uttcount = (0,) * 4
    __rawtokens, __tokens, __rawtypes, __types, __sentences, __utterances = ([],) * 6
    __shortest_words, __longest_words = (None,) * 2
    __alu, __ttr, __als = (0.0,) * 3

    # Syntactic Complexity Variables
    __yngve_score, __frazier_score, __string_yngve, __string_frazier, __cdensity, __idensity = (None,) * 6
    __flesch, __kincaid, __syllables, __asps, __aspu = (None,) * 5

    # Parsing Variables
    __treestrings, __maxdepth = (None,) * 2

    # Part-Of-Speech Variables
    __poscounts, __pos, __cwords, __fwords, __cfr, __u_cwords, __u_fwords = (None,) * 7

    # Language Modeling Variables
    __unigrams, __bigrams, __trigrams = (None,) * 3

    # Discourse Based Variables
    __adpu, __adps = (None,) * 2
    __splat = ""
    __dpu, __dps, __disfluencies = ({},) * 3

    # Frequency Distribution Variables
    __freq_dist = None

    # Object Declarations
    __ngramminator = FullNGramminator()
    __cleantokenizer = CleanTokenizer()
    __rawtokenizer = RawTokenizer()
    __sentenizer = CleanSentenizer()
    __postagger = NLTKPOSTagger()
    __treestring_gen = TreeStringParser()

    def __init__(self, text, ngramminator=FullNGramminator(), postagger=NLTKPOSTagger()):
        """
        Creates a SPLAT Object.
        """
        if os.path.exists(text):
            temp_text = ""
            temp_utts = []
            for line in open(text, 'r'):
                temp_utts.append(line.strip())
                temp_text += line.strip() + " "
            self.__splat = temp_text
            self.__utterances = temp_utts
        elif type(text) == str:
            self.__splat = text
            temp_utts = []
            for line in text.split("\n"):
                temp_utts.append(line.strip())
            self.__utterances = temp_utts
        else:
            raise ValueError("WARNING: SPLAT must be of type str or file.")

        self.__uttcount = len(self.__utterances)
        self.__sentences = self.__sentenizer.sentenize(self.__splat)
        if self.__sentences == []: self.__sentences = self.__utterances
        self.__sentcount = len(self.__sentences)
        self.__rawtokens = self.__rawtokenizer.tokenize(self.__splat)
        self.__tokens = self.__cleantokenizer.tokenize(self.__splat)
        self.__rawtypes = Util.typify(self.__rawtokens)
        self.__types = Util.typify(self.__tokens)
        self.__wordcount = Util.wordcount(self.__rawtokens)
        self.__unique_wordcount = Util.wordcount(self.__types)
        self.__ngramminator = ngramminator
        self.__postagger = postagger
        self.__ttr = Util.type_token_ratio(self.__types, self.__tokens)
        self.__alu = round(float(self.__wordcount) / float(self.__uttcount), 4) if self.__uttcount != 0 else 0.0
        self.__als = round(float(self.__wordcount) / float(self.__sentcount), 4) if self.__sentcount != 0 else 0.0
        temp_dpu = Util.count_disfluencies(self.__utterances)
        self.__dpu = temp_dpu[0]
        self.__adpu = temp_dpu[1]
        temp_dps = Util.count_disfluencies(self.__sentences)
        self.__dps = temp_dps[0]
        self.__adps = temp_dps[1]
        self.__disfluencies = Util.total_disfluencies(self.__dpu)

    ##### SYNTACTIC COMPLEXITY #########################################################################################

    def syllables(self):
        """ Returns the number of syllables in the SPLAT. """
        if self.__syllables is None:
            self.__syllables = cUtil.count_syllables(self.__tokens)
        return self.__syllables

    def average_sps(self):
        """ Returns the average number of syllables per sentence. """
        if self.__asps is None:
            self.__asps = float(self.syllables() / self.__sentcount)
        return self.__asps

    def average_spu(self):
        """ Returns the average number of syllables per utterance. """
        if self.__aspu is None:
            self.__aspu = float(self.syllables() / self.__uttcount)
        return self.__aspu

    def flesch_readability(self):
        """ Returns the flesch readability score. """
        if self.__flesch is None:
            self.__flesch = cUtil.calc_flesch_readability(self.__wordcount, self.__sentcount, self.syllables())
            return self.__flesch
        else:
            return self.__flesch

    def kincaid_grade_level(self):
        """ Returns the flesch-kincaid grade level score. """
        if self.__kincaid is None:
            self.__kincaid = cUtil.calc_flesch_kincaid(self.__wordcount, self.__sentcount, self.syllables())
            return self.__kincaid
        else:
            return self.__kincaid

    def content_density(self):
        """
        Returns the Content Density.
        Content Density is the ratio of open class words to closed class words.
        """
        if self.__cdensity is None:
            self.__cdensity = cUtil.calc_content_density(self.pos())
        return self.__cdensity

    def idea_density(self):
        """
        Returns the Idea Density.
        Idea Density is the ratio of prepositions to total word count.
        """
        if self.__idensity is None:
            self.__idensity = cUtil.calc_idea_density(self.pos())
        return self.__idensity

    def tree_based_yngve_score(self):
        """
        Returns the mean Yngve Score.
        Yngve score is... http://www.m-mitchell.com/papers/RoarkEtAl-07-SynplexityforMCI.pdf
        """
        if self.__yngve_score is None:
            trees = []
            for treestring in self.treestrings():
                trees.append(treestring)
            self.__yngve_score = cUtil.get_mean_yngve(trees)
            return self.__yngve_score
        else:
            return self.__yngve_score

    def string_based_yngve_score(self):
        """
        Returns the mean Yngve Score.
        Yngve score is... http://www.m-mitchell.com/papers/RoarkEtAl-07-SynplexityforMCI.pdf
        """
        print("WARNING: String-Based Yngve Score calculation is under review. Results may be inaccurate.")
        if self.__string_yngve is None:
            trees = []
            for treestring in self.treestrings():
                trees.append(treestring)
            self.__string_yngve = cUtil.get_total_mean_yngve(trees)
            return self.__string_yngve
        else:
            return self.__string_yngve

    def tree_based_frazier_score(self):
        """
        Returns the Frazier Score.
        Frazier score is... http://www.m-mitchell.com/papers/RoarkEtAl-07-SynplexityforMCI.pdf
        """
        if self.__frazier_score is None:
            trees = []
            for treestring in self.treestrings():
                trees.append(treestring)
            self.__frazier_score = cUtil.get_frazier_score(trees)
            return self.__frazier_score
        else:
            return self.__frazier_score

    def string_based_frazier_score(self):
        """
        Returns the Frazier Score.
        Frazier score is... http://www.m-mitchell.com/papers/RoarkEtAl-07-SynplexityforMCI.pdf
        """
        print("WARNING: String-Based Frazier Score calculation is under review, and thus not available at this time.")
        return ''

    ##### BASICS #######################################################################################################

    def sents(self):
        """ Returns a list of all sentences contained within the SPLAT. """
        return self.__sentences

    def utts(self):
        """ Returns a list of all utterances contained within the SPLAT. """
        return self.__utterances

    def rawtokens(self):
        """ Returns a list of unnormalized tokens. """
        return self.__rawtokens

    def tokens(self):
        """ Returns a list of normalized tokens. """
        return self.__tokens

    def rawtypes(self):
        """ Returns a list of unnormalized types. """
        return self.__rawtypes

    def types(self):
        """ Returns a list of normalized types. """
        return self.__types

    def wordcount(self):
        """ Returns the total word (token) count. """
        return self.__wordcount

    def unique_wordcount(self):
        """ Returns the unique word (type) count. """
        return self.__unique_wordcount

    def sentcount(self):
        """ Returns the total sentence count. """
        return self.__sentcount

    def uttcount(self):
        """ Returns the total utterance count. """
        return self.__uttcount

    def type_token_ratio(self):
        """ Returns the ratio of types to tokens. """
        return self.__ttr

    def average_utterance_length(self):
        """ Returns the average utterance length. """
        return self.__alu

    def average_sentence_length(self):
        """ Returns the average sentence length. """
        return self.__als

    def words_per_utterance(self):
        """ Prints the number of words in each utterance. """
        for item in self.__utterances:
            print(len(item.split(" ")))
        return ''

    def words_per_sentence(self):
        """ Prints the number of words in each sentence. """
        for item in self.__sentences:
            print(len(item.split(" ")))
        return ''

    def longest_words(self):
        """ Returns the longest words in the text."""
        if self.__longest_words is None:
            self.__longest_words = set([word for word in self.__tokens if len(word) == max(len(word) for word in self.__tokens)])
            return self.__longest_words
        else:
            return self.__longest_words

    def shortest_words(self):
        """ Returns the shortest words in the text."""
        if self.__shortest_words is None:
            self.__shortest_words = set([word for word in self.__tokens if len(word) == min(len(word) for word in self.__tokens)])
            return self.__shortest_words
        else:
            return self.__shortest_words

    ##### LANGUAGE MODELING ############################################################################################

    def unigrams(self):
        """ Returns a list of unigrams. """
        if self.__unigrams is None:
            self.__unigrams = self.__ngramminator.unigrams(self.__splat)
            return self.__unigrams
        else:
            return self.__unigrams

    def bigrams(self):
        """ Returns a list of bigrams. """
        if self.__bigrams is None:
            self.__bigrams = self.__ngramminator.bigrams(self.__splat)
            return self.__bigrams
        else:
            return self.__bigrams

    def trigrams(self):
        """ Returns a list of trigrams. """
        if self.__trigrams is None:
            self.__trigrams = self.__ngramminator.trigrams(self.__splat)
            return self.__trigrams
        else:
            return self.__trigrams

    def ngrams(self, n):
        """ Returns a list of n-grams.
        :param n: the size of the n-grams to be generated
        """
        if n == 1:
            return self.unigrams()
        elif n == 2:
            return self.bigrams()
        elif n == 3:
            return self.trigrams()
        else:
            return self.__ngramminator.ngrams(self.__splat, n)

    ##### PART-OF-SPEECH BASED #########################################################################################

    def pos(self):
        """ Returns a list of tuple pairs: (word, POS taggers). """
        if self.__pos is None:
            self.__pos = self.__postagger.tag(self.__splat)
        return self.__pos

    def content_function_ratio(self):
        """ Returns the ratio of content words to function words. """
        if self.__cfr is None:
            self.__cfr = Util.get_content_function_ratio(self.content_words(), self.function_words())
        return self.__cfr

    def content_words(self):
        """ Returns a list of content words. """
        if self.__cwords is None:
            self.__cwords = Util.get_content_words(self.__tokens)
        return self.__cwords

    def function_words(self):
        """ Returns a list of function words. """
        if self.__fwords is None:
            self.__fwords = Util.get_function_words(self.__tokens)
        return self.__fwords

    def unique_content_words(self):
        """ Returns a list of unique content words. """
        if self.__u_cwords is None:
            self.__u_cwords = Util.get_unique_content_words(self.__types)
        return self.__u_cwords

    def unique_function_words(self):
        """ Returns a list of unique function words. """
        if self.__u_fwords is None:
            self.__u_fwords = Util.get_unique_function_words(self.__types)
        return self.__u_fwords

    def pos_counts(self):
        """ Returns a dictionary with POS tags as keys and their frequencies as values. """
        if self.__poscounts is None:
            self.__poscounts = Util.get_pos_counts(self.pos())
        return self.__poscounts

    ##### PARSING ######################################################################################################

    def treestrings(self):
        """ Returns a list of parsers trees. """
        if self.__treestrings is None:
            self.__treestring_gen = TreeStringParser()
            self.__treestrings = self.__treestring_gen.get_parse_trees(self.__utterances)
        return self.__treestrings

    def drawtrees(self):
        """ Uses matplotlib and nltk to draw syntactic parsers trees. """
        Util.draw_trees(self.treestrings())
        return ''

    def max_depth(self):
        """ Returns the maxdepth of all syntactic parsers trees. """
        if self.__maxdepth is None:
            self.__maxdepth = Util.get_max_depth(self.treestrings())
        return self.__maxdepth

    ##### FREQUENCY DISTRIBUTIONS ######################################################################################

    def get_most_freq(self, x=None):
        """
        Returns the x most frequent words with their frequencies,
        or all words with their frequencies if x is not specified.
        :param x: the number of most frequent words to return
        """
        if self.__freq_dist is None:
            self.__freq_dist = Util.get_freq_dist(self.__tokens)
        if x is None:
            return self.__freq_dist.most_common()
        elif x > 0:
            return self.__freq_dist.most_common(x)
        else:
            return self.__freq_dist.most_common()

    def get_least_freq(self, x=None):
        """
        Returns the x least frequent words with their frequencies,
        or all words with their frequencies if x is not specified.
        :param x: the number of least frequent words to return
        """
        if self.__freq_dist is None:
            self.__freq_dist = Util.get_freq_dist(self.__tokens)

        most_common = self.__freq_dist.most_common()
        freq_dist = []
        count = 0
        for item in reversed(most_common):
                freq_dist.append(item)
        temp_freq = []

        if x is None:
            freq_dist = freq_dist
        else:
            for item in freq_dist:
                if count < int(x):
                    temp_freq.append(item)
                    count += 1

            freq_dist = temp_freq

        return freq_dist

    def plot_freq(self, x=None):
        """ Uses matplotlib to graph the frequency distribution.
        :param x:
        """
        if self.__freq_dist is None:
            self.__freq_dist = Util.get_freq_dist(self.__tokens)
        Util.plot_freq_dist(self.__freq_dist, x)
        return ''

    ##### DISCOURSE BASED ##############################################################################################

    def disfluencies_per_utterance(self):
        """ Displays the number of each type of disfluency per each utterance. """
        template = "{0:7}{1:7}{2:7}{3:7}{4:7}{5:7}{6:7}{7:7}{8:7}{9:50}"
        print(template.format("UM", "UH", "AH", "ER", "HM", "Pauses", "Reps", "Breaks", "Words", "Text"))
        for (k, v) in self.__dpu.items():
            print(template.format(str(v[0]), str(v[1]), str(v[2]), str(v[3]), str(v[4]), str(v[5]), str(v[6]), str(v[7]), str(v[8]), k))

        return ''

    def average_dpu(self):
        """ Return the average disfluencies per utterance. """
        return self.__adpu

    def disfluencies_per_sentence(self):
        """ Displays the number of each type of disfluency per each sentence. """
        template = "{0:7}{1:7}{2:7}{3:7}{4:7}{5:7}{6:7}{7:7}{8:7}{9:50}"
        print(template.format("UM", "UH", "AH", "ER", "HM", "Pauses", "Reps", "Breaks", "Words", "Text"))
        for (k, v) in self.__dps.items():
            print(template.format(str(v[0]), str(v[1]), str(v[2]), str(v[3]), str(v[4]), str(v[5]), str(v[6]), str(v[7]), str(v[8]), k))

        return ''

    def average_dps(self):
        """ Return the average disfluencies per sentence. """
        return self.__adps

    def disfluencies(self):
        """ Displays the total number of each type of disfluency. """
        d = self.__disfluencies
        print("Nasal\tUM\tHM\tNon-Nasal\tUH\tAH\tER\tSilent Pauses\tRepetitions\tBreaks")
        print(str(d["Nasal"]) + "\t" + str(d["UM"]) + "\t" + str(d["HM"]) + "\t" + str(d["Non-Nasal"]) +
              "\t\t" + str(d["UH"]) + "\t" + str(d["AH"]) + "\t" + str(d["ER"]) + "\t" + str(d["Pause"]) +
              "\t\t" + str(d["Repetitions"]) + "\t\t" + str(d["Break"]))

        return ''

    def dis(self):
        """ Return the raw disfluencies dictionary. """
        return self.__disfluencies

    ##### UNCATEGORIZED ################################################################################################

    def splat(self):
        return self.__splat

    def dump(self, out_file):
        json.dump(self.__dict__, out_file, default=jdefault)

    def dumps(self):
        return json.dumps(self.__dict__)

    def load(self, in_file):
        self.__dict__ = json.load(in_file)

    def loads(self, data_str):
        self.__dict__ = json.loads(data_str)


def jdefault(o):
    return o.__dict__
