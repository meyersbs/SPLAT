#!/usr/bin/python

from model.FullNGramminator import FullNGramminator
from tokenize.RawTokenizer import RawTokenizer
from tokenize.CleanTokenizer import CleanTokenizer
from sentenize.CleanSentenizer import CleanSentenizer
import base.Util as Util

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
	__bubble = ""
	__sentences = []
	__rawtokens = []
	__tokens = []
	__rawtypes = {}
	__types = {}
	__wordcount = 0
	__unique_wordcount = 0
	__sentcount = 0
	__ttr = 0.0
	__ngramminator = FullNGramminator()
	__cleantokenizer = CleanTokenizer()
	__rawtokenizer = RawTokenizer()
	__sentenizer = CleanSentenizer()
	def __init__(self, text, ngramminator=FullNGramminator()):
		if type(text) == str:
			self.__bubble = text
			self.__sentences = self.__sentenizer.sentenize(text)
			self.__sentcount = len(self.__sentences)
			self.__rawtokens = self.__rawtokenizer.tokenize(text)
			self.__tokens = self.__cleantokenizer.tokenize(text)
			self.__rawtypes = Util.typify(self.__rawtokens)
			self.__types = Util.typify(self.__tokens)
			self.__wordcount = Util.wordcount(self.__rawtokens)
			self.__unique_wordcount = Util.wordcount(self.__types)
			self.__ngramminator = ngramminator
			self.__ttr = Util.type_token_ratio(self.__types, self.__tokens)
		else:
			raise ValueError("textbubble must be of type str")

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
