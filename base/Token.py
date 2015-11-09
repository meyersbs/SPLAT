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

class Token(object):
	"""
	A Token object is simply a string.
	"""
	__text = ""
	def __init__(self, text):
		"""
		Creates a Token object from a given word.
		:param text:a word
		:type text:str
		:return:
		:rtype:
		"""
		if type(text) == str:
			self.__text = text
		else:
			raise ValueError("text must be of type str")

	def __str__(self):
		"""
		:return:the string representation of the Token object
		:rtype:str
		"""
		return self.__text

	def text(self):
		"""
		:return:the string representation of the Token object
		:rtype:str
		"""
		return self.__text