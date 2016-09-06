#!/usr/bin/env python3

##### PYTHON IMPORTS ###################################################################################################
import os, re

##### NLTK IMPORTS #####################################################################################################
from nltk import word_tokenize

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

class NLTKCleanTokenizer(Tokenizer):
	"""
	An NLTKCleanTokenizer provides the ability to tokenize a text input by converting it to lowercase and removing
	basic punctuation.
	"""
	def tokenize(self, text):
		raw_tokens = []
		if type(text) == str:
			if os.path.exists(text):
				raw_tokens = self.__tokenize_file(text)
			else:
				raw_tokens = text
		elif type(text) == list:
			raw_tokens = text
		else:
			raise ValueError("Text to tokenize must be of type str or type list.")

		clean_tokens = []
		for word in raw_tokens:
			clean_word = re.sub(r"[\.,!\?]", "", word)
			clean_tokens.append(clean_word.lower())

		clean_tokens = word_tokenize(" ".join(clean_tokens))

		return clean_tokens
