#!/usr/bin/env python3

##### PYTHON IMPORTS ###################################################################################################
import os

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

class NLTKRawTokenizer(Tokenizer):
	"""
	An NLTKRawTokenizer provides the ability to tokenize a text input ignoring case and punctuation.
	"""
	def tokenize(self, text):
		raw_text = ""
		raw_tokens = []
		if type(text) == str:
			if os.path.exists(text):
				raw_text = " ".join(self.__tokenize_file(text))
			else:
				raw_text = text
		elif type(text) == list:
			raw_text = " ".join(text)
		else:
			raise ValueError("Text to tokenize must be of type str or type list.")
		raw_tokens = word_tokenize(raw_text)
		
		return raw_tokens
