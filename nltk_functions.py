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
def get_most_frequent(text_file, x):
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

	return freq_dist.most_common(x)

def get_least_frequent(text_file, x):
	most_common = get_most_frequent(text_file, get_word_count(text_file))

	freq_dist = []
	count = 0
	for item in reversed(most_common):
		if count < x:
			freq_dist.append(item)
			count+=1

	return freq_dist

#Generate Tokens from a given text file, ignoring all annotations.
def get_tokens(text_file):
	f = open(text_file)
	raw = f.read()
	tokens = RegexpTokenizer(r'[^\d\s\:\(\)]+').tokenize(raw)

	#print(len(tokens))

	return tokens

#Generate Types from a given text file, ignoring all annotations.
def get_types(text_file):
	tokens = get_tokens(text_file)
	types = set(tokens)

	return types

#Generate Word Count from a given text file, ignoring all annotations.
def get_word_count(text_file):
	tokens = get_tokens(text_file)
	word_count = len(tokens)

	return word_count

#Generate a Unique Word Count from a given text file, ignoring all annotations.
def get_unique_word_count(text_file):
	types = get_types(text_file)
	unique_word_count = len(types)

	return unique_word_count

#Calculate the Lexical Diversity (num_tokens / num_types) for a given text file.
def get_lexical_diversity(text_file):
	num_types = get_unique_word_count(text_file)
	num_tokens = get_word_count(text_file)
	lexical_diversity = float(num_types) / num_tokens

	return lexical_diversity

#Look up a given word in a given text file and return its number of occurences.
def look_up_word(text_file, word):
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

	word_query = freq_dist[word]

	return word_query

##### DISPLAY COMMAND LIST ######################################
def display_command_list():
	command_list = '##### COMMAND LIST ##############################################'
	command_list += '\n# command \targ1 \targ2 \tdescription\t\t\t#'
	command_list += '\n#\t\t\t\t\t\t\t\t#'
	command_list += '\n# mf \t\tstr \tint \tMost Frequent Words in str\t#'
	command_list += '\n# ld \t\tstr \tint \tLexical Diversity\t\t#'
	command_list += '\n# lf \t\tstr \tint \tLeast Frequent Words in str\t#'
	command_list += '\n# s \t\tstr1 \tstr2 \tFind Occurrences of str2 in str1#'
	command_list += '\n# tk \t\tstr \t-- \tDisplay All Tokens\t\t#'
	command_list += '\n# ty \t\tstr \t-- \tDisplay All Types\t\t#'
	command_list += '\n# uwc \t\tstr \t-- \tDisplay Unique Word Count\t#'
	command_list += '\n# wc \t\tstr \t-- \tDisplay Total Word Count\t#'
	command_list += '\n#\t\t\t\t\t\t\t\t#'
	command_list += '\n# h \t\t-- \t-- \tShow Valid Commands.\t\t#'
	command_list += '\n# ~ \t\t-- \t-- \tShow Info.\t\t\t#'
	command_list += '\n# ! \t\t-- \t-- \tRun Tests.\t\t\t#'
	command_list += '\n# quit \t\t-- \t-- \tQuit Program.\t\t\t#'
	command_list += '\n#################################################################'
	print(command_list)
