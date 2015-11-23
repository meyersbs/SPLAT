#!/usr/bin/python

##### PYTHON IMPORTS ###################################################################################################
import re

##### SPLAT IMPORTS ####################################################################################################
from sentenizers.Sentenizer import Sentenizer

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

class CleanSentenizer(Sentenizer):
	"""
	A CleanSentenizer provides the functionality to generate a list of sentences from a text input with newlines
	removed.
	"""
	def sentenize(self, text):
		sentences = Sentenizer.sentenize(self, text)

		temp = []
		for sent in sentences:
			temp.append(re.sub(r"\n", "", sent))

		sentences = temp

		return sentences