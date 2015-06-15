#########################################################################################
# File Name: strip_timestamp.py
# Date Created: 06-08-2015
# Date Revised: 06-08-2015
# Author: Benjamin S. Meyers
# Email: bsm9339@rit.edu
# 	Advisor: Emily Prud'hommeaux
# 	Email: emilypx@rit.edu
# 	Advisor: Cissi Ovesdotter-Alm
# 	Email: coagla@rit.edu
#########################################################################################
import re

#A simple search and remove algorithm using regexes.
def strip_timestamp(text_file):

	with open(text_file) as f:
		new_text_name = text_file.strip('time.txt') + 'noTS.txt'
		new_text = open(new_text_name, 'w+')
		for line in f:
			new_text_line = ''
			if re.search(r'\(\d\d\:\d\d\:\d\d\)', line):
				new_text_line = line[11:]
			else:
				new_text_line = line
			new_text.write(new_text_line)

	new_text.close()

strip_timestamp('TD3_T2_facilitator_time.txt')
strip_timestamp('TD3_T2_participant_time.txt')
strip_timestamp('TD3_T2_Stereo_time.txt')
