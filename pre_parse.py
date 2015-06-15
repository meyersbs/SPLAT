#########################################################################################
# File Name: pre_parse.py
# Date Created: 06-11-2015
# Date Revised: 06-11-2015
# Author: Benjamin S. Meyers
# Email: bsm9339@rit.edu
# 	Advisor: Emily Prud'hommeaux
# 	Email: emilypx@rit.edu
# 	Advisor: Cissi Ovesdotter-Alm
# 	Email: coagla@rit.edu
#########################################################################################
import re

#A function to semi-automate utterance boundary insertion.
def pre_parse(text_file):

	with open(text_file) as f:
		new_name = text_file.strip('.txt') + '_UB.txt'
		new_file = open(new_name, 'w+')

		#Split the text file into a list of words.
		#There has to be a cleaner way to do this.
		for line in f:		
			list_words = str.split(line)
			#print(list_words)
			break

		#Remove all Praat markers.		
		new_list = []
		for word in list_words:
			if re.search(r'{SL}', word):
				new_list=new_list
			elif re.search(r'{NS}', word):
				new_list=new_list
			elif re.search(r'{BR}', word):
				new_list=new_list
			elif re.search(r'{LS}', word):
				new_list=new_list
			elif re.search(r'{LG}', word):
				new_list=new_list
			else:
				new_list.append(word.strip(' \n'))

		#Pre-Parse based on established rules.
		curr_line = ''
		found_and = False
		found_so = False
		found_its = False
		found_um = False
		found_could = False
		found_thats = False
		for new_word in new_list:
			if (re.search(r"THAT'S", new_word):
				found_thats = True
				curr_line+= (new_word + ' ')
			elif found_thats and re.search(r'OK', new_word):
				curr_line = curr_line[:-6]
				new_file.write(curr_line)
				curr_line = ('\n' + "THAT'S OK ")
				found_thats = False
			elif (re.search(r'OK', new_word)
				or re.search(r'YEAH', new_word)
				or re.search(r'ACTUALLY', new_word)):
				new_file.write(curr_line)
				curr_line = ('\n' + new_word + ' ')
			elif (re.search(r'MHM', new_word)
				or re.search(r'YEP', new_word)
				or re.search(r'PERFECT', new_word)
				or re.search(r'GOOD', new_word)):
				new_file.write(curr_line)
				curr_line = ('\n' + new_word)
				new_file.write(curr_line)
				curr_line = '\n'
			elif re.search(r'AND', new_word):
				found_and = True
				curr_line+= (new_word + ' ')
			elif found_and and (re.search(r'THEN', new_word)
				or re.search(r'NOW', new_word)):
				curr_line = curr_line[:-4]
				new_file.write(curr_line)
				curr_line = ('\n' + 'AND ' + new_word + ' ')
				found_and = False
			elif re.search(r'SO', new_word):
				found_so = True
				curr_line+= (new_word + ' ')
			elif found_so and (re.search(r"I'LL", new_word)
				or re.search(r"I'M", new_word)
				or re.search(r"^I$", new_word)):
				curr_line = curr_line[:-3]
				new_file.write(curr_line)
				curr_line = ('\n' + "SO " + new_word + ' ')
				found_so = False
			elif re.search(r"IT'S", new_word):
				found_its = True
				curr_line+= (new_word + ' ')
			elif found_its and re.search(r'ALRIGHT', new_word):
				curr_line = curr_line[:-5]
				new_file.write(curr_line)
				curr_line = ('\n' + "IT'S ALRIGHT")
				new_file.write(curr_line)
				curr_line = '\n'
				found_its = False
			elif re.search(r"UM", new_word):
				found_um = True
				curr_line+= (new_word + ' ')
			elif found_um and re.search(r'NOW', new_word):
				curr_line = curr_line[:-3]
				new_file.write(curr_line)
				curr_line = ('\n' + "UM NOW ")
				found_um = False
			elif re.search(r"COULD", new_word):
				found_could = True
				curr_line+= (new_word + ' ')
			elif found_could and re.search(r'YOU', new_word):
				curr_line = curr_line[:-6]
				new_file.write(curr_line)
				curr_line = ('\n' + "COULD YOU ")
				found_could = False
			else:
				found_and = False
				found_so = False
				found_its = False
				found_um = False
				found_could = False
				found_thats = False
				curr_line+= (new_word + ' ')
		
		new_file.write(curr_line)
				
pre_parse('TD3_T2_Stereo.txt')
