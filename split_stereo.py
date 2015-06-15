#########################################################################################
# File Name: split_stereo.py
# Date Created: 06-10-2015
# Date Revised: 06-10-2015
# Author: Benjamin S. Meyers
# Email: bsm9339@rit.edu
# 	Advisor: Emily Prud'hommeaux
# 	Email: emilypx@rit.edu
# 	Advisor: Cissi Ovesdotter-Alm
# 	Email: coagla@rit.edu
#########################################################################################
import re

#Split a single combined transcript into separate participant and facilitator transcripts.
def split_stereo(text_file):

	with open(text_file) as f:
		new_fac_name = text_file[:7] + 'facilitator_time.txt'
		new_sub_name = text_file[:7] + 'participant_time.txt'
		new_fac = open(new_fac_name, 'w+')
		new_sub = open(new_sub_name, 'w+')
		for line in f:
			new_text_line = ''
			if re.search(r'F\:', line):
				new_fac.write(line)
			elif re.search(r'S\:', line):
				new_sub.write(line)
			else:
				new_fac.write(line)
				new_sub.write(line)

	new_fac.close()
	new_sub.close()

split_stereo('TD3_T2_Stereo_time.txt')
