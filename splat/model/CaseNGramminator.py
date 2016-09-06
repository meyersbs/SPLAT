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
class CaseNGramminator(NGramminator):
	"""
	A CaseNGramminator provides the functionality to generate ngrams for a given text sequence.
	All characters in the given text are lowercased before being ngramminated.
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
		temp_text = []
		if type(text) == str:
			temp_text = text.lower().split()
		elif type(text) == list:
			temp_text = text
			text = []
			for temp_word in temp_text:
				text.append(temp_word.lower())
			temp_text = text
		else:
			raise ValueError

		text = temp_text

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
