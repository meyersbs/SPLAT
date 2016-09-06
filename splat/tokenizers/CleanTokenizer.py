#!/usr/bin/env python3

##### PYTHON IMPORTS ###################################################################################################
import re

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

class CleanTokenizer(Tokenizer):
	"""
	A CleanTokenizer provides the ability to tokenize a text input by converting it to lowercase and removing
	basic punctuation.
	"""
	def tokenize(self, text):
		raw_tokens = Tokenizer.tokenize(self, text)
		clean_tokens = []
		
		temp = []
		for token in raw_tokens:
			if token != "" and token != " ":
				temp.append(token.strip("\n"))

		raw_tokens = temp

		for word in raw_tokens:
			clean_word = re.sub(r"[\.,!\?]", "", word)
			clean_tokens.append(clean_word.lower())
		
		return clean_tokens
