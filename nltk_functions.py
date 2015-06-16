#################################################################
# File Name: nltk_functions.py					#
# Date Created: 06-15-2015					#
# Date Revised: 06-16-2015					#
# Author: Benjamin S. Meyers					#
# Email: bsm9339@rit.edu					#
# 	Advisor: Emily Prud'hommeaux				#
# 	Email: emilypx@rit.edu					#
# 	Advisor: Cissi Ovesdotter-Alm				#
# 	Email: coagla@rit.edu					#
#################################################################
from nltk.corpus import gutenberg
from nltk.probability import FreqDist
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize
import nltk
import random
import re

##### GLOBAL VARIABLES ##########################################
startup_info = '#################################################################'
startup_info +='\n# CLAAP - Corpus & Linguistics Annotating & Analyzing in Python #'
startup_info +='\n# Version 0.00 \tJune 15, 2015 \t3:55 PM UTC \t\t\t#'
startup_info +='\n# Developed by Benjamin S. Meyers\t\t\t\t#'
startup_info +='\n#\t\t\t\t\t\t\t\t#'
startup_info +='\n# This application may not be copied, altered, or distributed \t#'
startup_info +='\n# without written consent from the product owner. \t\t#'
startup_info +='\n# \t\t\t\t\t\t\t\t#'
startup_info +='\n# Type "~" for more information. \t\t\t\t#'
startup_info +='\n#\t\t\t\t\t\t\t\t#'
startup_info +='\n# Welcome to CLAAP! Type "h" for help.\t\t\t\t#'
startup_info +='\n#################################################################'

exit_messages = [("If you're happy and you know it, CLAAP your hands!"),("Petrichor\n(noun)\na pleasant smell that frequently accompanies the first rain after a long period of warm, dry weather."), ("Syzygy is the only word in English that contains three 'y's."), ("Tmesis is the only word in the English language that begins with 'tm'."), ("In Old English, bagpipes were called 'doodle sacks'."), ("A 'quire' is two-dozen sheets of paper."), ("'Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo' is a grammatically correct sentence in American English."), ("J.R.R. Tolkien coined the term 'glossopoeia,' which is the act of inventing languages."), ("Beowulf is an English work, but if you try to read it in its original form, it will look like gibberish!"), ("'To Be Or Not To Be' = 'U+0032 U+0042 U+2228 U+0021 U+0032 U+0042'")]

more_info = "\nThis application was developed by Benjamin S. Meyers beginning on June 1, 2015 for an Undergraduate Research Internship at the Rochester Institute of Technology. CLAAP's primary application is to allow an easy-to-use tool for Linguists to annotate and analyze corpora consisting of discourse and dialogue.\n\tVersion 0.00\tJune 15, 2015\t3:55 PM UTC\n\tVersion 0.01\tJune 16, 2015\t11:29 AM UTC"

moby_dick = nltk.Text(gutenberg.words('melville-moby_dick.txt'))

douglas = "\n           o o o   .-\'\"\"\"\'-.   o o o             DON\'T PANIC!"
douglas +="\n           \\\|/  .'         '.  \|//"
douglas +="\n            \-;o/             \o;-/"
douglas +="\n            // ;               ; \\\\"
douglas +="\n           //__; :.         .: ;__\\\\"
douglas +="\n          `-----\\'.'-.....-'.'/-----'           444    2222222"
douglas +="\n                 '.'.-.-,_.'.'                 4444   222   222"
douglas +="\n                   '(  (..-'                  44 44         22"
douglas +="\n      |              '-'                     44  44        22"
douglas +="\n  |           |                             444444444     22"
douglas +="\n |  |  |    |                                    44      22"
douglas +="\n     |     |  |                                  44    222"
douglas +="\n| |   |     %%%                                  44   222222222"
douglas +="\n    ___    _\|/_         _%%_____"
douglas +="\n\,-\' \'_|   \___/      __/___ \'   \\"                    
douglas +="\n/\"\"----\'          ___/__  \'   \'\'  \__%__       __%____%%%___"
douglas +="\n                 /   \" \'   _%__ \'   \'   \_____/____ \'  __ \" \\"
douglas +="\n           __%%_/__\'\' __     \'   _%_\'_   \     \"\'    _%__ \'\' \_"
douglas +="\n __/\__%%_/_/___\___ \'\'   \'_%_\"___   \"    \_%__ \'___\"     \"\'   \\"
douglas +="\n/_________________\____\'_RIP Douglas___\"_______\_______\'_____\"__\\"
douglas +="\n"

##### FUNCTIONS #################################################

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

	print(len(tokens))

	return tokens

#Generate Types from a given text file, ignoring all annotations.
def get_types(text_file):
	types = []
	with open(text_file) as f:
		for line in f:
			line.replace('  ', ' ')
			line.replace('\n', '')
			word_line = line.split()
			for word in word_line:
				types.append(word.strip(' \n'))

		for word in types:
			if re.search(r'{SL}', word):
				types.remove(word)
			elif re.search(r'{NS}', word):
				types.remove(word)
			elif re.search(r'{BR}', word):
				types.remove(word)
			elif re.search(r'{LS}', word):
				types.remove(word)
			else:
				types = types

	return types

#Generate Word Count from a given text file, ignoring all annotations.
def get_word_count(text_file):
	types = get_types(text_file)
	word_count = len(types)

	return word_count

def get_lexical_diversity(text_file):
	types = get_types(text_file)
	tokens = get_tokens(text_file)
	lexical_diversity = len(types) / len(tokens)

	return lexical_diversity

##### DISPLAY COMMAND LIST ######################################
def display_command_list():
	command_list = '##### COMMAND LIST ##############################################'
	command_list += '\n# command \targ1 \targ2 \tdescription\t\t\t#'
	command_list += '\n#\t\t\t\t\t\t\t\t#'
	command_list += '\n# f \t\tstr \tint \tget_freqs(str, int)\t\t#'
	command_list += '\n# h \t\t-- \t-- \tdisplay_command_list()\t\t#'
	command_list += '\n# tk \t\tstr \t-- \tget_tokens(str)\t\t\t#'
	command_list += '\n# ty \t\tstr \t-- \tget_types(str)\t\t\t#'
	command_list += '\n# ! \t\t-- \t-- \trun_tests()\t\t\t#'
	command_list += '\n# q \t\t-- \t-- \tquit program.\t\t\t#'
	command_list += '\n#################################################################'
	print(command_list)
