#!/usr/bin/python

from base.Sent import Sent
from model.FullNGramminator import FullNGramminator
import re

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
	__types = {}
	__ngramminator = FullNGramminator()
	def __init__(self, text, ngramminator=FullNGramminator()):
		if type(text) == str:
			self.__bubble = text
			for sentence in text.split("\n"):
				if sentence != "" and sentence != "\n":
					self.__sentences.append(sentence)
					for word in sentence.split():
						self.__rawtokens.append(word)
			temp_types = {}
			for word in self.__rawtokens:
				if word not in temp_types.keys():
					temp_types[word] = 1
				else:
					temp_types[word] += 1
			self.__types = temp_types
			self.__ngramminator = ngramminator
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

	def raw_tokens(self):
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
		clean_tokens = []
		for token in self.__rawtokens:
			clean_tokens.append(token.lower().strip(".").strip(",").strip("!").strip("?"))
		return clean_tokens

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
		return len(self.__rawtokens)

	def unique_wordcount(self):
		"""
		:return:the number of types in the TextBubble
		:rtype:int
		"""
		return len(self.__types.keys())

	def sentcount(self):
		"""
		:return:the number of sentences in the TextBubble
		:rtype:int
		"""
		return len(self.__sentences)

	def type_token_ratio(self):
		"""
		:return:the type-token ratio of the TextBubble
		:rtype:float
		"""
		return round((float((self.unique_wordcount / self.wordcount) * 100), 4))

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
			output += "[" + str(count) + "] " + sentence.string + "\n"
			count += 1
		output += "Sentence Count: " + str(self.sentcount) + "\n"
		output += "===== Tokens:\n"
		output += self.tokens + "\n"
		output += "Word Count: " + str(self.wordcount) + "\n"
		output += "===== Types:\n"
		output += self.__types + "\n"
		output += "Unique Word Count: " + str(self.unique_wordcount) + "\n"
		output += "===== Type-Token Ratio:\n"
		output += str(self.type_token_ratio) + "\n"
