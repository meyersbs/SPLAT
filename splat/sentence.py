#!/usr/bin/env python

""" Defines a wrapper object for sentences. """

__author__ = "Benjamin S. Meyers"
__copyright__ = "Copyright 2015-2017, Benjamin S. Meyers"
__credits__ = ["Benjamin S. Meyers"]
__version__ = "1.0.0"
__maintainer__ = "Benjamin S. Meyers"
__email__ = "ben@splat-library.org"
__status__ = "Development"

#### IMPORTS ###################################################################
from splat import CONFIG, LOGGER, UNCERTAINTY_MAP, Word
from splat.chunkers import Conll2000Chunker
from splat.classifiers import (UncertaintyClassifier, PolitenessClassifier)
from splat.lemmatizers import WordNetLemmatizer
from splat.stemmers import NLTKStemmer
from splat.syllablizers import CMUDictSyllablizer
from splat.taggers import NLTKPOSTagger
from splat.tokenizers import NLTKTokenizer


class Sentence(object):
    def __init__(self, sentence, pos_tagger=NLTKPOSTagger, stemmer=NLTKStemmer,
                 lemmatizer=WordNetLemmatizer, tokenizer=NLTKTokenizer,
                 syllablizer=CMUDictSyllablizer, chunker=Conll2000Chunker,
                 uncertainty_classifier=UncertaintyClassifier,
                 politeness_classifier=PolitenessClassifier):
        """
        Instantiate a Sentence object with the given parameters.
        :param sentence:
        :param pos_tagger:
        :param stemmer:
        :param lemmatizer:
        :param tokenizer:
        :param syllablizer:
        :param chunker:
        :param uncertainty_classifier:
        :param politeness_classifier:
        """
        self._pos_tagger = pos_tagger
        self._stemmer = stemmer
        self._chunker = chunker
        self._lemmatizer = lemmatizer
        self._tokenizer = tokenizer
        self._syllablizer = syllablizer
        self._uncertainty_classifier = uncertainty_classifier
        self._politeness_classifier = politeness_classifier
        
        self._sentence = sentence
        self._words = list()

        self._treestring = None
        self._dependency_parse = None

        # Pragmatic Metrics
        self._uncertainty, self._politeness, self._formality, \
            self._informativeness, self._implicature = (None,)*5

        # Complexity Metrics
        self._yngve_min, self._yngve_max, self._yngve_mean = (None,)*3
        self._frazier_min, self._frazier_max, self._frazier_mean = (None,)*3
        self._pdensity, self._cdensity = (None,)*2

        # Readability Metrics
        self._flesch, self._flesch_kincaid, self._gunning_fog, self._smog, \
            self._dale_chall, self._fry, self._forcast = (None,)*7

        words = [word for word in self._tokenizer.tokenize(self._sentence)]
        tags = self._pos_tagger.tag(words)
        stems = self._stemmer.stem(words)
        chunks = self._chunker.chunk(words)
        lemmas = self._lemmatizer.lemmatize(words)
        syllables = self._syllablizer.syllabize(words)
        for w,p,s,c,l,y in zip(words, tags, stems, chunks, lemmas, syllables):
            self._words.append(Word(w, p, s, c, l, y))

        self._length = len(self._words)

    def _get_sentence(self):
        return self._sentence

    def _set_sentence(self, sentence):
        self._sentence = sentence
    sentence = property(_get_sentence,_set_sentence)

    def _get_words(self):
        return self._words

    def _set_words(self, words):
        self._words = words
    words = property(_get_words,_set_words)

    def _get_length(self):
        return self._length

    def _set_length(self, length):
        self._length = length
    length = property(_get_length,_set_length)

    def _get_treestring(self):
        return self._treestring

    def _set_treestring(self, treestring):
        self._treestring = treestring
    treestring = property(_get_treestring,_set_treestring)

    def _get_dependency_parse(self):
        return self._dependency_parse

    def _set_dependency_parse(self, dependency_parse):
        self._dependency_parse = dependency_parse
    dependency_parse = property(_get_dependency_parse,_set_dependency_parse)

    def _get_uncertainty(self):
        return self._uncertainty

    def _set_uncertainty(self, uncertainty):
        self._uncertainty = uncertainty
    uncertainty = property(_get_uncertainty,_set_uncertainty)

    def _get_politeness(self):
        return self._politeness

    def _set_politeness(self, politeness):
        self._politeness = politeness
    politeness = property(_get_politeness,_set_politeness)

    def _get_formality(self):
        return self._formality

    def _set_formality(self, formality):
        self._formality = formality
    formality = property(_get_formality,_set_formality)

    def _get_informativeness(self):
        return self._informativeness

    def _set_informativeness(self, informativeness):
        self._informativeness = informativeness
    informativeness = property(_get_informativeness,_set_informativeness)

    def _get_implicature(self):
        return self._implicature

    def _set_implicature(self, implicature):
        self._implicature = implicature
    implicature = property(_get_implicature,_set_implicature)

    def _get_yngve_min(self):
        return self._yngve_min

    def _set_yngve_min(self, yngve_min):
        self._yngve_min = yngve_min
    yngve_min = property(_get_yngve_min,_set_yngve_min)

    def _get_yngve_max(self):
        return self._yngve_max

    def _set_yngve_max(self, yngve_max):
        self._yngve_max = yngve_max
    yngve_max = property(_get_yngve_max,_set_yngve_max)

    def _get_yngve_mean(self):
        return self._yngve_mean

    def _set_yngve_mean(self, yngve_mean):
        self._yngve_mean = yngve_mean
    yngve_mean = property(_get_yngve_mean,_set_yngve_mean)

    def _get_yngve(self):
        return [self._yngve_min, self._yngve_mean, self._yngve_max]

    yngve = property(_get_yngve)

    def _get_frazier_min(self):
        return self._frazier_min

    def _set_frazier_min(self, frazier_min):
        self._frazier_min = frazier_min
    frazier_min = property(_get_frazier_min,_set_frazier_min)

    def _get_frazier_max(self):
        return self._frazier_max

    def _set_frazier_max(self, frazier_max):
        self._frazier_max = frazier_max
    frazier_max = property(_get_frazier_max,_set_frazier_max)

    def _get_frazier_mean(self):
        return self._frazier_mean

    def _set_frazier_mean(self, frazier_mean):
        self._frazier_mean = frazier_mean
    frazier_mean = property(_get_frazier_mean,_set_frazier_mean)

    def _get_frazier(self):
        return [self._frazier_min, self._frazier_mean, self._frazier_max]
    frazier = property(_get_frazier)

    def _get_pdensity(self):
        return self._pdensity

    def _set_pdensity(self, pdensity):
        self._pdensity = pdensity
    pdensity = property(_get_pdensity,_set_pdensity)

    def _get_cdensity(self):
        return self._cdensity

    def _set_cdensity(self, cdensity):
        self._cdensity = cdensity
    cdensity = property(_get_cdensity,_set_cdensity)

    def _get_complexity(self):
        d = {'yngve_min': self._yngve_min, 'yngve_max': self._yngve_max,
             'yngve_mean': self._yngve_mean, 'frazier_min': self._frazier_min,
             'frazier_max': self._frazier_max,
             'frazier_mean': self._frazier_mean, 'pdensity': self._pdensity,
             'cdensity': self._cdensity}
        return d
    complexity = property(_get_complexity)

    def _get_flesch(self):
        return self._flesch

    def _set_flesch(self, flesch):
        self._flesch = flesch
    flesch = property(_get_flesch,_set_flesch)

    def _get_flesch_kincaid(self):
        return self._flesch_kincaid

    def _set_flesch_kincaid(self, flesch_kincaid):
        self._flesch_kincaid = flesch_kincaid
    flesch_kincaid = property(_get_flesch_kincaid,_set_flesch_kincaid)

    def _get_gunning_fog(self):
        return self._gunning_fog

    def _set_gunning_fog(self, gunning_fog):
        self._gunning_fog = gunning_fog
    gunning_fog = property(_get_gunning_fog,_set_gunning_fog)

    def _get_smog(self):
        return self._smog

    def _set_smog(self, smog):
        self._smog = smog
    smog = property(_get_smog,_set_smog)

    def _get_dale_chall(self):
        return self._dale_chall

    def _set_dale_chall(self, dale_chall):
        self._dale_chall = dale_chall
    dale_chall = property(_get_dale_chall,_set_dale_chall)

    def _get_fry(self):
        return self._fry

    def _set_fry(self, fry):
        self.fry_ = fry
    fry = property(_get_fry,_set_fry)

    def _get_forcast(self):
        return self._forcast

    def _set_forcast(self, forcast):
        self._forcast = forcast
    forcast = property(_get_forcast,_set_forcast)

    def _get_readability(self):
        d = {'flesch': self._flesch, 'flesch_kincaid': self._flesch_kincaid,
             'gunning_fog': self._gunning_fog, 'smog': self._smog,
             'dale_chall': self._dale_chall, 'fry': self._fry,
             'forcast': self._forcast}
        return d
    readability = property(_get_readability)

    def __str__(self):
        return self._sentence

    def __dict__(self):
        d = {'sentence': self._sentence, 'words': self._words,
             'treestring': self._treestring,
             'dependency_parse': self._dependency_parse,
             'uncertainty': self._uncertainty, 'politeness': self._politeness,
             'formality': self._formality,
             'informativeness': self._informativeness,
             'implicature': self._implicature, 'yngve_min': self._yngve_min,
             'yngve_max': self._yngve_max, 'yngve_mean': self._yngve_mean,
             'frazier_min': self._frazier_min, 'frazier_max': self._frazier_max,
             'frazier_mean': self._frazier_mean, 'pdensity': self._pdensity,
             'cdensity': self._cdensity, 'flesch': self._flesch,
             'flesch_kincaid': self._flesch_kincaid,
             'gunning_fog': self._gunning_fog, 'smog': self._smog,
             'dale_chall': self._dale_chall, 'fry': self._fry,
             'forcast': self._forcast}

        return d
