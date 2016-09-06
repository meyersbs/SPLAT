#!/usr/bin/env python3

##### PYTHON IMPORTS ###################################################################################################
from abc import abstractmethod

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

class NGramminator:
	"""
	An NGramminator provides the functionality to generate ngrams for a given text sequence.
	"""
	def __init__(self):
		"""
		Creates an NGramminator object.
		"""
		pass

	@abstractmethod
	def ngrams(self, text, n):
		"""
		Generates a list of ngrams of size n.
		:param text:the text selection to ngramminate
		:type text:str
		:param n:the size of each ngram
		:type n:int
		:return:a list of ngrams of size n
		:rtype:list
		"""
		raise NotImplementedError

	@abstractmethod
	def unigrams(self, text):
		"""
		Generates a list of unigrams.
		:param text:the text selection to ngramminate
		:type text:str
		:return:a list of unigrams
		:rtype:list
		"""
		return self.ngrams(text, 1)

	@abstractmethod
	def bigrams(self, text):
		"""
		Generates a list of bigrams.
		:param text:the text selection to ngramminate
		:type text:str
		:return:a list of bigrams
		:rtype:list
		"""
		return self.ngrams(text, 2)

	@abstractmethod
	def trigrams(self, text):
		"""
		Generates a list of trigrams.
		:param text:the text selection to ngramminate
		:type text:str
		:return:a list of trigrams
		:rtype:list
		"""
		return self.ngrams(text, 3)
