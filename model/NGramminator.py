#!/usr/bin/python

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

class NGramminator:
	"""
	An NGramminator provides the functionality to generate ngrams for a given text sequence.
	"""
	name = ""
	def __init__(self):
		"""
		Creates an NGramminator object.
		"""
		pass

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
		text = iter(text)
		history = []
		while n > 1:
			history.append(next(text))
			n -= 1
		for item in text:
			history.append(item)
			yield tuple(history)
			del history[0]

	def unigrams(self, text):
		"""
		Generates a list of unigrams.
		:param text:the text selection to ngramminate
		:type text:str
		:return:a list of unigrams
		:rtype:list
		"""
		return self.ngrams(text, 1)

	def bigrams(self, text):
		"""
		Generates a list of bigrams.
		:param text:the text selection to ngramminate
		:type text:str
		:return:a list of bigrams
		:rtype:list
		"""
		return self.ngrams(text, 2)

	def trigrams(self, text):
		"""
		Generates a list of trigrams.
		:param text:the text selection to ngramminate
		:type text:str
		:return:a list of trigrams
		:rtype:list
		"""
		return self.ngrams(text, 3)

