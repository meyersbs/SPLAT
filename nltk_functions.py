#########################################################################################
# File Name: nltk_functions.py
# Date Created: 06-15-2015
# Date Revised: 06-15-2015
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
	command_list = '##################################################'
	command_list += '\ncommand arg1 \targ2 \tdescription\n'
	command_list += '\nf \tstr \tint \tget_freqs(str, int)'
	command_list += '\nh \t-- \t-- \tdisplay_command_list()'
	command_list += '\nt \tstr \t-- \tget_tokens(str)'
	command_list += '\n! \t-- \t-- \trun_accuracy_tests()'
	command_list += '\nq \t-- \t-- \tquit program.'
	command_list += '\n##################################################'
	print(command_list)

##### MAIN #######################################
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
	elif command[0] == 'q' and len(command) == 1:
		break
	else:
		print('Invalid Command.\nFor Help, type \'h\'.')
