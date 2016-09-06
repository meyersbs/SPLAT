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

class QuarteroniDialogActAnnotator:
	__dialog_acts = {1:'Info-Request',				2:'Action-Request',		3:'Yes-Answer',			4:'No-Answer',
                     5:'Answer',					6:'Offer',				7:'Report-On-Action',	8:'Inform',
                     9:'Greet',						10:'Quit',				11:'Apology',			12:'Thank',
                     13:'Clarification-Request',	14:'Acknowledgment',	15:'Filler',			16:'Other'}
	__print_acts = ' 1\t' + __dialog_acts[1] + '\t\t 2\t' + __dialog_acts[2] + '\n'
	__print_acts += ' 3\t' + __dialog_acts[3] + '\t\t 4\t' + __dialog_acts[4] + '\n'
	__print_acts += ' 5\t' + __dialog_acts[5] + '\t\t\t 6\t' + __dialog_acts[6] + '\n'
	__print_acts += ' 7\t' + __dialog_acts[7] + '\t 8\t' + __dialog_acts[8] + '\n'
	__print_acts += ' 9\t' + __dialog_acts[9] + '\t\t\t10\t' + __dialog_acts[10] + '\n'
	__print_acts += '11\t' + __dialog_acts[11] + '\t\t\t12\t' + __dialog_acts[12] + '\n'
	__print_acts += '13\t' + __dialog_acts[13] + '\t14\t' + __dialog_acts[14] + '\n'
	__print_acts += '15\t' + __dialog_acts[15] + '\t\t\t16\t' + __dialog_acts[16] + '\n'
	def __init__(self):
		pass

	def annotate(self, text):
		"""
		Given a selection of text, semi-automatically insert dialog act and speaker annotation with input from the User.
		"""
		annotated_text = ""
		for line in text.split("\n"):
			looping = True
			annotation = ' ('
			while looping:
				print('Please select a dialog act for:\t' + line + '\nOr enter \'0\' to continue...')
				print(self.__print_acts)
				marker = input()
				if int(marker) == 0:
					annotation = annotation[:-2] + ')\n'
					looping = False
					break
				elif int(marker) in self.__dialog_acts.keys():
					annotation += self.__dialog_acts[int(marker)] + ', '

			annotated_text += line + annotation

		return annotated_text
