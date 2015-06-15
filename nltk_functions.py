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
##################################################

#A simple NLTK function
def get_freqs(text_file):
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

	print(freq_dist.most_common(50))

#Generate Tokens from a given text file, ignoring
#	all annotations.
def get_tokens(text_file):
	f = open(text_file)
	raw = f.read()
	tokens = RegexpTokenizer(r'[^\d\s\:\(\)]+').tokenize(raw)

	return tokens

##### TEST FUNCTIONS #############################
def check_tokenize_accuracy():
	if get_tokens(AS1_f_NT) == get_tokens(AS1_f_NT):
		print('SUCCESS!')
	else:
		print('FAILURE!')

##### MAIN #######################################
get_freqs(AS1_f_NT)
get_freqs(AS1_f_TS)
check_tokenize_accuracy()
