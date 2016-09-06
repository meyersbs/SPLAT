#!/usr/bin/env python3

##### SPLAT IMPORTS ####################################################################################################
from splat.tokenizers.Tokenizer import Tokenizer

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

class RawTokenizer(Tokenizer):
	"""
	A RawTokenizer provides the ability to tokenize a text input ignoring case and punctuation.
	"""
	def tokenize(self, text):
		raw_tokens = Tokenizer.tokenize(self, text)

		temp = []
		for token in raw_tokens:
			if token != "" and token != " ":
				temp.append(token.strip("\n"))

		raw_tokens = temp

		return raw_tokens