#!/usr/bin/env python3

##### SPLAT IMPORTS ####################################################################################################
from splat.model.NGramminator import NGramminator

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
class RawNGramminator(NGramminator):
	"""
	A RawNGramminator provides the functionality to generate ngrams for a given text sequence.
	No text normalization occurs.
	"""
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
		if type(text) == str:
			text = text.split()
		elif type(text) == list:
			text = text
		else:
			raise ValueError

		ngram_list = []
		for i in range(len(text)-n+1):
			ngram = []
			for j in range(0,n):
				ngram.append(text[i+j])
			ngram_list.append(tuple(ngram))
		return ngram_list

	def unigrams(self, text):
		return self.ngrams(text, 1)

	def bigrams(self, text):
		return self.ngrams(text, 2)

	def trigrams(self, text):
		return self.ngrams(text, 3)