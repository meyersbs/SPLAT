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

class MeyersDialogActAnnotator:
	__dialog_acts = {1:'Info-Request',			2:'Action-Request',		3:'Action-Suggest',	4:'Answer-Yes',
                     5:'Answer-No',				6:'Answer-Neutral',		7:'Apology',		8:'Thanks',
                     9:'Clarification-Request',	10:'Acknowledgment',	11:'Filler',		12:'Inform',
                     13:'Other'}
	__print_acts = ' 1\t' + __dialog_acts[1] + '\t 2\t' + __dialog_acts[2] + '\t 3\t' + __dialog_acts[3] + '\n'
	__print_acts += ' 4\t' + __dialog_acts[4] + '\t 5\t' + __dialog_acts[5] + '\t 6\t' + __dialog_acts[6] + '\n'
	__print_acts += ' 7\t' + __dialog_acts[7] + '\t\t 8\t' + __dialog_acts[8] + '\t\t 9\t' + __dialog_acts[9] + '\n'
	__print_acts += '10\t' + __dialog_acts[10] + '\t11\t' + __dialog_acts[11] + '\t\t12\t' + __dialog_acts[12] + '\n'
	__print_acts += '13\t' + __dialog_acts[13] + '\n'

	def __init__(self):
		pass

	def annotate(self, text):
		"""
		Given a selection of text, semi-automatically insert dialog act and speaker annotation with input from the User.
		"""
		annotated_text = ""
		for line in text:
			looping = True
			annotation = ' ('
			while looping:
				print('Please select a dialog act for:\t' + line + '\nOr enter \'0\' to continue...')
				print(self.__print_acts)
				marker = input()
				if int(marker) == 0:
					annotation = annotation[:-2] + ')\n'
					print(annotation)
					#looping = False
					break
				elif int(marker) in self.__dialog_acts.keys():
					annotation += self.__dialog_acts[int(marker)] + ', '

			annotated_text += line + annotation

		return annotated_text