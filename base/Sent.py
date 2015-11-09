#!/usr/bin/python

from base import Token

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

class Sent(object):
	"""
	A Sentence object is essentially a list of Token objects.
	"""
	tokens = []
	def __init__(self, sentence):
		if type(sentence) == str:
			for token in sentence.split():
				self.tokens.append(Token(token))
		elif type(sentence) == list:
			for token in sentence:
				self.tokens.append(Token(token))
		else:
			raise ValueError("sentence must be of type str or list")

	def __str__(self):
		"""
		:return:the string representation of the Sentence object
		:rtype:str
		"""
		return " ".join(self.tokens)

	def words(self):
		"""
		:return:a list of Token objects
		:rtype:list
		"""
		return self.tokens

	def wordcount(self):
		return len(self.tokens)

	def string(self):
		"""
		:return:the string representation of the Sentence object
		:rtype:str
		"""
		return " ".join(self.tokens)
