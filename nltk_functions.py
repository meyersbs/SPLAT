#########################################################################################
# File Name: nltk_functions.py
# Date Created: 06-15-2015
# Date Revised: 06-16-2015
# Author: Benjamin S. Meyers
# Email: bsm9339@rit.edu
# 	Advisor: Emily Prud'hommeaux
# 	Email: emilypx@rit.edu
# 	Advisor: Cissi Ovesdotter-Alm
# 	Email: coagla@rit.edu
#########################################################################################
from nltk.probability import FreqDist
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize
import random
import re

##### GLOBAL VARIABLES ###########################
AS1_f_TS = 'AS1_T2_facilitator_time.txt'
AS1_f_NT = 'AS1_T2_facilitator_noTS.txt'
AS1_p_TS = 'AS1_T2_participant_time.txt'
AS1_p_NT = 'AS1_T2_participant_noTS.txt'
AS1_s_TS = 'AS1_T2_Stereo_time.txt'
AS1_s_NT = 'AS1_T2_Stereo_noTS.txt'

AS2_f_TS = 'AS2_T2_facilitator_time.txt'
AS2_f_NT = 'AS2_T2_facilitator_noTS.txt'
AS2_p_TS = 'AS2_T2_participant_time.txt'
AS2_p_NT = 'AS2_T2_participant_noTS.txt'
AS2_s_TS = 'AS2_T2_Stereo_time.txt'
AS2_s_NT = 'AS2_T2_Stereo_noTS.txt'

AS3_f_TS = 'AS3_T2_facilitator_time.txt'
AS3_f_NT = 'AS3_T2_facilitator_noTS.txt'
AS3_p_TS = 'AS3_T2_participant_time.txt'
AS3_p_NT = 'AS3_T2_participant_noTS.txt'
AS3_s_TS = 'AS3_T2_Stereo_time.txt'
AS3_s_NT = 'AS3_T2_Stereo_noTS.txt'

TD1_f_TS = 'TD1_T2_facilitator_time.txt'
TD1_f_NT = 'TD1_T2_facilitator_noTS.txt'
TD1_p_TS = 'TD1_T2_participant_time.txt'
TD1_p_NT = 'TD1_T2_participant_noTS.txt'
TD1_s_TS = 'TD1_T2_Stereo_time.txt'
TD1_s_NT = 'TD1_T2_Stereo_noTS.txt'

TD2_f_TS = 'TD2_T2_facilitator_time.txt'
TD2_f_NT = 'TD2_T2_facilitator_noTS.txt'
TD2_p_TS = 'TD2_T2_participant_time.txt'
TD2_p_NT = 'TD2_T2_participant_noTS.txt'
TD2_s_TS = 'TD2_T2_Stereo_time.txt'
TD2_s_NT = 'TD2_T2_Stereo_noTS.txt'

TD3_f_TS = 'TD3_T2_facilitator_time.txt'
TD3_f_NS = 'TD3_T2_facilitator_noTS.txt'
TD3_p_TS = 'TD3_T2_participant_time.txt'
TD3_p_NS = 'TD3_T2_participant_noTS.txt'
TD3_s_TS = 'TD3_T2_Stereo_time.txt'
TD3_s_NS = 'TD3_T2_Stereo_noTS.txt'

exit_messages = [("If you're happy and you know it, CLAAP your hands!"),("Petrichor\n(noun)\na pleasant smell that frequently accompanies the first rain after a long period of warm, dry weather."), ("Syzygy is the only word in English that contains three 'y's."), ("Tmesis is the only word in the English language that begins with 'tm'."), ("In Old English, bagpipes were called 'doodle sacks'."), ("A 'quire' is two-dozen sheets of paper."), ("'Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo' is a grammatically correct sentence in American English."), ("J.R.R. Tolkien coined the term 'glossopoeia,' which is the act of inventing languages."), ("Beowulf is an English work, but if you try to read it in its original form, it will look like gibberish!"), ("'To Be Or Not To Be' = 'U+0032 U+0042 U+2228 U+0021 U+0032 U+0042'")]

more_info = "\nThis application was developed by Benjamin S. Meyers beginning on June 1, 2015 for an Undergraduate Research Internship at the Rochester Institute of Technology. CLAAP's primary application is to allow an easy-to-use tool for Linguists to annotate and analyze corpora consisting of discourse and dialogue.\n\tVersion 0.00\tJune 15, 2015\t3:55 PM UTC\n\tVersion 0.01\tJune 16, 2015\t11:29 AM UTC"

##### FUNCTIONS ##################################

#Display the top x most frequent tokens (words) in the given text_file.
def get_freqs(text_file, x):
	all_words = get_tokens(text_file)
	new_words = []
	for token in all_words:
		#print(token)
		if re.match(r'^F', token):
			new_words = new_words
		elif re.match(r'^S', token):
			new_words = new_words
		elif re.match(r'^T', token):
			new_words = new_words
		elif re.match(r'^SILENCE', token):
			new_words = new_words
		else:
			new_words.append(token)

	freq_dist = FreqDist(new_words)

	print(freq_dist.most_common(x))

#Generate Tokens from a given text file, ignoring all annotations.
def get_tokens(text_file):
	f = open(text_file)
	raw = f.read()
	tokens = RegexpTokenizer(r'[^\d\s\:\(\)]+').tokenize(raw)

	return tokens

##### TEST FUNCTIONS #############################
def check_tokenize_accuracy():
	if get_tokens(AS1_f_NT) == get_tokens(AS1_f_NT):
		return 'ACCURATE!'
	else:
		return 'INACCURATE!'

def run_accuracy_tests():
	print('##### RUNNING TESTS ####################')
	print('\nget_tokens(str) status: ' + check_tokenize_accuracy())
	print('\n########################################')

##### DISPLAY COMMAND LIST #######################
def display_command_list():
	command_list = '#################################################################'
	command_list += '\n# command \targ1 \targ2 \tdescription\t\t\t#'
	command_list += '\n#\t\t\t\t\t\t\t\t#'
	command_list += '\n# f \t\tstr \tint \tget_freqs(str, int)\t\t#'
	command_list += '\n# h \t\t-- \t-- \tdisplay_command_list()\t\t#'
	command_list += '\n# t \t\tstr \t-- \tget_tokens(str)\t\t\t#'
	command_list += '\n# ! \t\t-- \t-- \trun_accuracy_tests()\t\t#'
	command_list += '\n# q \t\t-- \t-- \tquit program.\t\t\t#'
	command_list += '\n#################################################################'
	print(command_list)

##### MAIN #######################################
def main():
	print('#################################################################')
	print('# CLAAP - Corpus & Linguistics Annotating & Analyzing in Python #')
	print('# Version 0.00 \tJune 15, 2015 \t3:55 PM UTC \t\t\t#')
	print('# Developed by Benjamin S. Meyers\t\t\t\t#')
	print('#\t\t\t\t\t\t\t\t#')
	print('# This application may not be copied, altered, or distributed \t#')
	print('# without written consent from the product owner. \t\t#')
	print('# \t\t\t\t\t\t\t\t#')
	print('# Type "~" for more information. \t\t\t\t#')
	print('#\t\t\t\t\t\t\t\t#')
	print('# Welcome to CLAAP! Type "h" for help.\t\t\t\t#')
	print('#################################################################')
	while(True):
		user_command = raw_input('Please provide a command: ')
		command = word_tokenize(user_command)
		#print(command)
		if command[0] == 't' and len(command) == 2:
			get_tokens(command[1])
		elif command[0] == 'f' and len(command) == 3:
			get_freqs(command[1], int(command[2]))
		elif command[0] == 'h' and len(command) == 1:
			display_command_list()
		elif command[0] == '!' and len(command) == 1:
			run_accuracy_tests()
		elif command[0] == '~' and len(command) == 1:
			print(more_info)
		elif len(command) == 1 and command[0] == '42':
			print('\nLook at you, getting all existential on me!\n')
		elif command[0] == 'q' and len(command) == 1:
			print('\n' + random.choice(exit_messages) + '\n')
			break
		else:
			print('Invalid Command.\nFor Help, type \'h\'.')

if __name__ == "__main__":
    main()
