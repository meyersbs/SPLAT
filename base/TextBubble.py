#!/usr/bin/python

from model.FullNGramminator import FullNGramminator
from tokenizers.RawTokenizer import RawTokenizer
from tokenizers.CleanTokenizer import CleanTokenizer
from sentenizers.CleanSentenizer import CleanSentenizer
from tag.POSTagger import POSTagger
from parse.TreeStringGenerator import TreeStringGenerator
import base.Util as Util
import os.path

########################################################################################################################
##### INFORMATION ######################################################################################################
### @PROJECT_NAME:		SPLAT: Speech Processing and Linguistic Annotation Tool										 ###
### @VERSION_NUMBER:																								 ###
### @PROJECT_SITE:		github.com/meyersbs/SPLAT																     ###
### @AUTHOR_NAME:		Benjamin S. Meyers																			 ###
### @CONTACT_EMAIL:		bsm9339@rit.edu																				 ###
### @LICENSE_TYPE:																									 ###
########################################################################################################################
########################################################################################################################

class TextBubble:
	"""
	A TextBubble is a bubble of text. It can be a single word, a paragraph, or even a whole novel!
	The TextBubble object makes it super simple to extract features from a selection of text.
	"""
	# Word Count, Unique Word Count, Sentence Count, Utterance Count
	__wordcount, __unique_wordcount, __sentcount, __uttcount = 0, 0, 0, 0
	# Content-Function Ratio, Average Utterance Length, Type-Token Ratio
	__cfr, __alu, __ttr = 0.0, 0.0, 0.0
	# Sentences, Utterances, Raw Tokens, Tokens, Tokens with POS Tags
	__sentences, __utterances, __rawtokens, __tokens, __pos = [], [], [], [], []
	# Content Words, Function Words, Unique Content Words, Unique Function Words
	__c_words, __f_words, __uc_words, __uf_words = [], [], [], []
	# Raw Types, Types
	__rawtypes, __types = {}, {}
	__bubble = ""
	__ngramminator = FullNGramminator()
	__cleantokenizer = CleanTokenizer()
	__rawtokenizer = RawTokenizer()
	__sentenizer = CleanSentenizer()
	__postagger = POSTagger()
	__treestring_gen = TreeStringGenerator()
	__treestrings = []
	def __init__(self, text, ngramminator=FullNGramminator(), postagger=POSTagger()):
		if os.path.exists(text):
			temp_text = ""
			temp_utts = []
			for line in open(text, 'r'):
				temp_utts.append(line.strip())
				temp_text += line.strip() + " "
			self.__bubble = temp_text
			self.__utterances = temp_utts
		elif type(text) == str:
			self.__bubble = text
			temp_utts = []
			for line in text.split("\n"):
				temp_utts.append(line.strip())
			self.__utterances = temp_utts
		else:
			raise ValueError("textbubble must be of type str")

		self.__uttcount = len(self.__utterances)
		self.__sentences = self.__sentenizer.sentenize(self.__bubble)
		self.__sentcount = len(self.__sentences)
		self.__rawtokens = self.__rawtokenizer.tokenize(self.__bubble)
		self.__tokens = self.__cleantokenizer.tokenize(self.__bubble)
		self.__rawtypes = Util.typify(self.__rawtokens)
		self.__types = Util.typify(self.__tokens)
		self.__wordcount = Util.wordcount(self.__rawtokens)
		self.__unique_wordcount = Util.wordcount(self.__types)
		self.__ngramminator = ngramminator
		self.__postagger = postagger
		self.__ttr = Util.type_token_ratio(self.__types, self.__tokens)
		self.__pos = self.__postagger.tag(self.__bubble)
		self.__alu = round(float(self.__wordcount) / float(self.__uttcount), 4)
		self.__c_words = Util.get_content_words(self.__tokens)
		self.__f_words = Util.get_function_words(self.__tokens)
		self.__uc_words = Util.get_unique_content_words(self.__types)
		self.__uf_words = Util.get_unique_function_words(self.__types)
		self.__cfr = Util.get_content_function_ratio(self.__tokens)
		self.__treestring_gen = TreeStringGenerator()
		self.__treestrings = self.__treestring_gen.get_parse_trees(self.__sentences)

	def bubble(self):
		"""
		:return:the raw TextBubble
		:rtype:str
		"""
		return self.__bubble

	def sents(self):
		"""
		:return:a list of sentences
		:rtype:list
		"""
		return self.__sentences

	def utts(self):
		"""
		:return:a list of utterances
		:rtype:list
		"""
		return self.__utterances

	def rawtokens(self):
		"""
		A list of tokens that have not been normalized.
		:return:a list of tokens
		:rtype:list
		"""
		return self.__rawtokens

	def tokens(self):
		"""
		A list of tokens that have been normalized.
		:return:a list of tokens
		:rtype:list
		"""
		return self.__tokens

	def rawtypes(self):
		"""
		:return:a list of types
		:rtype:list
		"""
		return self.__rawtypes

	def types(self):
		"""
		:return:a list of types
		:rtype:list
		"""
		return self.__types

	def wordcount(self):
		"""
		:return:the total wordcount of the TextBubble
		:rtype:int
		"""
		return self.__wordcount

	def unique_wordcount(self):
		"""
		:return:the number of types in the TextBubble
		:rtype:int
		"""
		return self.__unique_wordcount

	def sentcount(self):
		"""
		:return:the number of sentences in the TextBubble
		:rtype:int
		"""
		return self.__sentcount

	def uttcount(self):
		"""
		:return:the number of utterances in the TextBubble
		:rtype:int
		"""
		return self.__uttcount

	def type_token_ratio(self):
		"""
		:return:the type-token ratio of the TextBubble
		:rtype:float
		"""
		return self.__ttr

	def unigrams(self):
		"""
		:return:a list of unigrams
		:rtype:list of tuples
		"""
		return self.__ngramminator.unigrams(self.__bubble)

	def bigrams(self):
		"""
		:return:a list of bigrams
		:rtype:list of tuples
		"""
		return self.__ngramminator.bigrams(self.__bubble)

	def trigrams(self):
		"""
		:return:a list of trigrams
		:rtype:list of tuples
		"""
		return self.__ngramminator.trigrams(self.__bubble)

	def ngrams(self, n):
		"""
		:return:a list of ngrams of size n
		:rtype:list of tuples
		"""
		return self.__ngramminator.ngrams(self.__bubble, n)

	def pos(self):
		"""
		:return:a list of tuples(word, tag)
		:rtype:list of tuples
		"""
		return self.__pos

	def average_utterance_length(self):
		#TODO
		return self.__alu

	def content_function_ratio(self):
		return self.__cfr

	def content_words(self):
		return self.__c_words

	def function_words(self):
		return self.__f_words

	def unique_content_words(self):
		return self.__uc_words

	def unique_function_words(self):
		return self.__uf_words

	def treestrings(self):
		return self.__treestrings

	def drawtrees(self):
		Util.draw_trees(self.__treestrings)
		return ''

	def words_per_utterance(self):
		for item in self.__utterances:
			print(len(item.split(" ")))
		return ''

	def words_per_sentence(self):
		for item in self.__sentences:
			print(len(item.split(" ")))
		return ''

	def splat(self):
		"""
		:return:a massive SPLAT of the different features in the TextBubble
		:rtype:str
		"""
		output = "===== Bubble:\n"
		output += self.__bubble + "\n"
		output += "===== Sentences:\n"
		count = 0
		for sentence in self.__sentences:
			output += "[" + str(count) + "] " + str(sentence) + "\n"
			count += 1
		output += "Sentence Count: " + str(self.__sentcount) + "\n"
		output += "===== Tokens:\n"
		output += str(self.__tokens) + "\n"
		output += "Word Count: " + str(self.__wordcount) + "\n"
		output += "===== Types:\n"
		output += str(self.__types) + "\n"
		output += "Unique Word Count: " + str(self.__unique_wordcount) + "\n"
		output += "===== Type-Token Ratio:\n"
		output += str(self.__ttr) + "\n"

		return output
