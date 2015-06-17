#################################################################
# File Name: nltk_functions.py					#
# Date Created: 06-15-2015					#
# Date Revised: 06-17-2015					#
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
from nltk_variables import *
import nltk
import random
import re

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

	#print(len(tokens))

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
	command_list += '\n# tk \t\tstr \t-- \tget_tokens(str)\t\t\t#'
	command_list += '\n# ty \t\tstr \t-- \tget_types(str)\t\t\t#'
	command_list += '\n#\t\t\t\t\t\t\t\t#'
	command_list += '\n# h \t\t-- \t-- \tShow Valid Commands.\t\t#'
	command_list += '\n# ~ \t\t-- \t-- \tShow Info.\t\t\t#'
	command_list += '\n# ! \t\t-- \t-- \tRun Tests.\t\t\t#'
	command_list += '\n# quit \t\t-- \t-- \tQuit Program.\t\t\t#'
	command_list += '\n#################################################################'
	print(command_list)
