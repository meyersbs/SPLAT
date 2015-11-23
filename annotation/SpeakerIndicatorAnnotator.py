#!/usr/bin/python

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

class SpeakerIndicatorAnnotator:
	def __init__(self):
		pass

	def annotate(self, text):
		annotated_text = ""
		for line in text.split("\n"):
			if line != "":
				print('Please enter a speaker marker for:\t' + line)
				marker = input()
				annotated_text += marker + ": " + line + "\n"

		return annotated_text