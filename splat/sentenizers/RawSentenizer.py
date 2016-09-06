#!/usr/bin/env python3

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

class RawSentenizer(Sentenizer):
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
		sentences = Sentenizer.sentenize(self, text)

		return sentences