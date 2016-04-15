#!/usr/bin/python3.4

##### PYTHON IMPORTS ###################################################################################################
import re

##### SPLAT IMPORTS ####################################################################################################
from splat.tokenizers.Tokenizer import Tokenizer

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

class PunctTokenizer(Tokenizer):
	"""
	A PuncTokenizer provides the ability to tokenize a text input, including punctuation as separate tokens.
	"""
	def tokenize(self, text):
		punc_tokens = []
		raw_tokens = Tokenizer.tokenize(self, text)
		
		temp = []
		for token in raw_tokens:
			temp_tokens = re.findall(r"[\w']+|[\.,!?;:]", token)
			for temp_token in temp_tokens:
				if token != "" and token != " " and token != ' ' and token != '':
					temp.append(temp_token.lower())

		punc_tokens = temp
		
		return punc_tokens