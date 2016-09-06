#!/usr/bin/env python3

##### PYTHON IMPORTS ###################################################################################################
from abc import abstractmethod
import os.path

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

class Tokenizer:
	"""
	A Tokenizer provides the functionality to generate a list of tokens from a text input.
	"""
	def __init__(self):
		"""
		Creates a Tokenizer object.
		"""
		pass

	@staticmethod
	def __tokenize_list(text):
		"""
		Returns a list of tokens.
		:param text:a list of strings to be tokenized
		:type text:list
		:return:a list of tokens
		:rtype:list
		"""
		tokens = []
		for item in text:
			for word in item.split(" "):
				tokens.append(word)

		return tokens

	@staticmethod
	def __tokenize_string(text):
		"""
		Returns a list of tokens.
		:param text:a string to be tokenized
		:type text:str
		:return:a list of tokens
		:rtype:list
		"""
		tokens = []
		for word in text.split(" "):
			tokens.append(word.strip("\n"))

		return tokens

	@staticmethod
	def __tokenize_file(text):
		"""
		Returns a list of tokens.
		:param text:a list of strings to be tokenized
		:type text:filename
		:return:a list of tokens
		:rtype:list
		"""
		tokens = []
		with open(text, 'r') as f:
			for line in f:
				for word in line.split(" "):
					tokens.append(word)

		return tokens

	@abstractmethod
	def tokenize(self, text):
		raw_tokens = []
		if type(text) == str:
			if os.path.exists(text):
				raw_tokens = self.__tokenize_file(text)
			else:
				raw_tokens = self.__tokenize_string(text)
		elif type(text) == list:
			raw_tokens = self.__tokenize_list(text)
		else:
			raise ValueError("Text to tokenize must be of type str or type list.")

		return raw_tokens