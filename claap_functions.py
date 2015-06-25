#!/usr/bin/python

from matplotlib import *
from nltk.probability import FreqDist
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize
from termcolor import *

import csv
import nltk
import random
import re

versions = ['Version 1.00\t06-24-15\t04:24 PM UTC', 'Version 0.10\t06-16-15\t11:29 AM UTC', 'Version 0.00\t06-15-15\t03:55 PM UTC']

# Print the Usage Instructions to stdout.
def display_command_list():
	command_list = '##### COMMAND LIST ##############################################'
	command_list += '\n# command \targ1 \targ2 \tdescription\t\t\t#'
	command_list += '\n#\t\t\t\t\t\t\t\t#'
	command_list += '\n# mf \t\tstr \t*int \tMost Frequent Words in str\t#'
	command_list += '\n# lf \t\tstr \t*int \tLeast Frequent Words in str\t#'
	command_list += '\n# pfd \t\tstr \t*int \tPlot Frequency Distribution\t#'
	command_list += '\n# pos \t\tstr \t-- \tDisplay Parts of Speech\t\t#'
	command_list += '\n# psc \t\tstr \t-- \tDisplay POS Counts\t\t#'
	command_list += '\n# s \t\tstr1 \tstr2 \tFind Occurrences of str2 in str1#'
	command_list += '\n# tokens \tstr \t-- \tDisplay All Tokens\t\t#'
	command_list += '\n# ttr \t\tstr \t-- \tType-Token Ratio\t\t#'
	command_list += '\n# types \tstr \t-- \tDisplay All Types\t\t#'
	command_list += '\n# uwc \t\tstr \t-- \tDisplay Unique Word Count\t#'
	command_list += '\n# wc \t\tstr \t-- \tDisplay Total Word Count\t#'
	command_list += '\n#\t\t\t\t\t\t\t\t#'
	command_list += '\n# --usage \t-- \t-- \tShow Usage Info.\t\t#'
	command_list += '\n# --commands \t-- \t-- \tShow Valid Commands.\t\t#'
	command_list += '\n# --info \t-- \t-- \tShow Info.\t\t\t#'
	command_list += '\n# --version \t-- \t-- \tDisplay Installed Version.\t#'
	command_list += '\n#################################################################'
	print(command_list)

def print_usage_instructions():
	usage = '\nInvalid command. For a list of available commands, use ' + colored('--commands', 'green') + '.'
	usage+= '\nCommands look like this: ' + colored('claap', 'blue') + ' ' + colored('COMMAND', 'green') + ' ' + colored('arg1 arg2 ...', 'red')
	usage+= '\n'

	print(usage)

# Print the program info to stdout.
def info():
	prog_info = '#################################################################'
	prog_info +='\n# CLAAP - Corpus & Linguistics Annotating & Analyzing in Python #'
	prog_info +='\n# Version 1.00 \tJune 24, 2015 \t04:24 PM UTC \t\t\t#'
	prog_info +='\n# Developed by Benjamin S. Meyers\t\t\t\t#'
	prog_info +='\n#\t\t\t\t\t\t\t\t#'
	prog_info +='\n# This application may not be copied, altered, or distributed \t#'
	prog_info +='\n# without written consent from the product owner. \t\t#'
	prog_info +='\n# \t\t\t\t\t\t\t\t#'
	prog_info +='\n# For documentation, visit: https://github.com/meyersbs/CLAAP \t#'
	prog_info +='\n# \t\t\t\t\t\t\t\t#'
	prog_info +="\n# If you're happy and you know it, CLAAP your hands!\t\t#"
	prog_info +='\n#\t\t\t\t\t\t\t\t#'
	prog_info +='\n#################################################################'

	print(prog_info)

def version_info():
	print(versions[0])

#Calculate the frequency distribution.
def get_freq_dist(text_file):
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

	return freq_dist

#Generate a list of tokens.
def get_tokens(text_file):
	f = open(text_file)
	raw = f.read()
	tokens = RegexpTokenizer(r'[^\d\s\:\(\)]+').tokenize(raw)

	return tokens

#Generate a list of types.
def get_types(text_file):
	tokens = get_tokens(text_file)
	types = set(tokens)

	return types

#Generate a Total Word Count.
def get_word_count(text_file):
	tokens = get_tokens(text_file)
	word_count = len(tokens)

	return word_count

#Generate a Unique Word Count.
def get_unique_word_count(text_file):
	types = get_types(text_file)
	unique_word_count = len(types)

	return unique_word_count

#Calculate the Type-Token Ratio.
def get_TTR(text_file):
	num_types = get_unique_word_count(text_file)
	num_tokens = get_word_count(text_file)
	type_token_ratio = float(num_types) / num_tokens * 100

	return round(type_token_ratio, 2)

#Tag all Types with Parts of Speech.
def tag_pos(text_file):
	tokens = get_tokens(text_file)
	parts_of_speech = nltk.pos_tag(tokens)

	return parts_of_speech

#Calculate the Total Number for each POS.
def get_pos_counts(text_file):
	pos = dict(tag_pos(text_file))
	
	pos_counts = {}
	for (k,v) in pos.items():
		if v in pos_counts.keys():
			pos_counts[v] += 1
		else:
			pos_counts.update({v:1})

	return pos_counts

#Plot the frequency distribution.
def plot_freq_dist(text_file, x=None):
	freq_dist = get_freq_dist(text_file)

	if x == -1:
		freq_dist.plot()
	else:
		freq_dist.plot(int(x))

#Display the top x most frequent tokens.
def get_most_frequent(text_file, x=None):
	freq_dist = get_freq_dist(text_file)

	if(x == None):
		return freq_dist.most_common()
	else:
		return freq_dist.most_common(int(x))

#Display the top x least frequent tokens.
def get_least_frequent(text_file, x=None):
	most_common = get_most_frequent(text_file, get_word_count(text_file))

	freq_dist = []
	count = 0

	if x == None:
		freq_dist = most_common
	else:
		for item in reversed(most_common):
			if count < int(x):
				freq_dist.append(item)
				count+=1

	return freq_dist
