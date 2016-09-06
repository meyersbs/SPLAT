#!/usr/bin/env python3

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

class SpeakerIndicatorAnnotator:
	def __init__(self):
		pass

	def annotate(self, text):
		"""
		Given a selection of text, semi-automatically insert dialog act and speaker annotation with input from the User.
		"""
		annotated_text = ""
		for line in text.split("\n"):
			if line != "":
				print('Please enter a speaker marker for:\t' + line)
				marker = input()
				annotated_text += marker + ": " + line + "\n"

		return annotated_text