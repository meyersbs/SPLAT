#!/usr/bin/env python3

##### PYTHON IMPORTS ###################################################################################################
import os

##### NLTK IMPORTS #####################################################################################################
from nltk import sent_tokenize

##### SPLAT IMPORTS ####################################################################################################
from splat.sentenizers.Sentenizer import Sentenizer

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

class NLTKSentenizer(Sentenizer):
	"""
	A RawSentenizer provides the functionality to generate a list of unprocessed sentences from a text input.
	"""
	def sentenize(self, text):
		"""

		:param text:
		:type text:
		:return:
		:rtype:
		"""
		sentences = ""
		if type(text) == str:
			if os.path.exists(text):
				sentences = " ".join(self.__sentenize_file(self, text))
			else:
				sentences = text
		elif type(text) == list:
			sentences = " ".join(text)
		else:
			raise ValueError("Text to sentenize must be of type str or type list.")

		sentences = sent_tokenize(sentences)

		return sentences
