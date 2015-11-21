#!/usr/bin/python

import re

from nltk.tree import Tree
from nltk.probability import FreqDist

from corpus.Util import Stopwords

########################################################################################################################
##### INFORMATION ######################################################################################################
### @PROJECT_NAME:		SPLAT: Speech Processing and Linguistic Annotation Tool										 ###
### @VERSION_NUMBER:																								 ###
### @PROJECT_SITE:		github.com/meyersbs/SPLAT																     ###
### @AUTHOR_NAME:		Benjamin S. Meyers																			 ###
### @CONTACT_EMAIL:		bsm9339@rit.edu																				 ###
### @LICENSE_TYPE:																									 ###
########################################################################################################################
########################################################################################################################

open_class_list = ['NN', 'NNS', 'NNP', 'NNPS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS', 'FW']
ignore_list = ['LS', 'SYM', 'UH', 'LBR', 'RBR', '-LBR-', '-RBR-', '$', '``', '"', '\'\'', '(', ')', '()', '( )', '\,', '\-\-', '\.', '\:', 'SBAR', 'SBARQ']
proposition_list = ['CC', 'CD', 'DT', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS', 'IN', 'CC', 'PDT', 'POS', 'PP$', 'PRP$', 'TO', 'WDT', 'WP', 'WPS', 'WRB']

def typify(tokens):
	"""
	Returns a dictionary of unique types with their frequencies.
	:param tokens:a list of tokens
	:type tokens:list
	:return:a dictionary of unique types with their frequencies.
	:rtype:dict
	"""
	temp_types = {}
	for word in tokens:
		if word not in temp_types.keys():
			temp_types[word] = 1
		else:
			temp_types[word] += 1

	return sorted(temp_types.items())

def wordcount(text):
	if type(text) == str:
		return len(text.split(" "))
	elif type(text) == list:
		return len(text)
	else:
		raise ValueError("Text to count words for must be of type str or of type list.")

def type_token_ratio(types, tokens):
	return round(float(len(types)) / float(len(tokens)) * 100, 4)

def get_content_words(tokens):
	""" Get a list of all content words. """
	content_words = []
	for word in tokens:
		if word.lower() not in Stopwords:
			content_words.append(word)

	return content_words

def get_unique_content_words(types):
	""" Get a list of unique content words. """
	content_words = []
	for (word, count) in types:
		if word.lower() not in Stopwords:
			content_words.append(word)

	return content_words

def get_function_words(tokens):
	""" Get a list of all function words. """
	function_words = []
	for word in tokens:
		if word.lower() in Stopwords:
			function_words.append(word)

	return function_words

def get_unique_function_words(types):
	""" Get a list of unique function words. """
	function_words = []
	for (word, count) in types:
		if word.lower() in Stopwords:
			function_words.append(word)

	return function_words

def get_content_function_ratio(tokens):
	""" Calculate the content-function word ratio. """
	content = get_content_words(tokens)
	function = get_function_words(tokens)

	ratio = float(len(content)) / float(len(function))

	return round(ratio, 4)

def draw_trees(treestrings):
	""" Draws pictures of each parse-tree-string using Matplotlib. """
	for tree_string in treestrings:
		print(tree_string)
		sentence = Tree.fromstring(tree_string)
		sentence.draw()

	return ''

def get_pos_counts(tagged_text):
	""" Calculate the total number of types for each part of speech tag. """
	pos_counts = {}
	for item in tagged_text:
		if item[1] in pos_counts.keys():
			pos_counts[item[1]] += 1
		else:
			pos_counts.update({item[1]: 1})

	return pos_counts

def get_max_depth(treestrings):
	""" Calculate the max depths for each parse tree. """
	depths = []

	for treestring in treestrings:
		curr_depth, max_depth = 0, 0
		for word in treestring.split(" "):
			for char in word:
				if char == "(":
					curr_depth += 1
				elif char == ")":
					curr_depth -= 1
				else:
					pass

				if curr_depth > max_depth:
					max_depth = curr_depth
			depths.append(max_depth)

	max_depth = 0
	for val in depths:
		if val > max_depth:
			max_depth = val

	return max_depth

def get_freq_dist(tokens):
	""" Calculate the frequency distribution for the given input_file. """
	new_words = []
	for token in tokens:
		new_words.append(token)

	return FreqDist(new_words)

def plot_freq_dist(freq_dist, x=None):
	""" Plot the frequency distribution for the given input_file. """
	if x is None:
		freq_dist.plot()
	else:
		freq_dist.plot(int(x))

	return ''

def count_disfluencies(utterances):
	disfluencies = {}
	for utt in utterances:
		disfluencies[utt] = []
		um_count = 0
		uh_count = 0
		ah_count = 0
		er_count = 0
		hm_count = 0
		pause_count = 0
		repetition_count = 0
		break_count = 0
		last_word = ""
		for word in utt.split(" "):
			if word.lower() == "UM":
				um_count += 1
			elif word.lower() == "UH":
				uh_count += 1
			elif word.lower() == "AH":
				ah_count += 1
			elif word.lower() == "ER":
				er_count += 1
			elif word.lower() == "HM":
				hm_count += 1
			elif word.lower() == "{sl}":
				pause_count += 1
			elif word == last_word:
				repetition_count += 1
				last_word = word
			elif re.search(r"-$", word):
				break_count += 1
			else:
				pass

		disfluencies[utt].append(um_count)
		disfluencies[utt].append(uh_count)
		disfluencies[utt].append(ah_count)
		disfluencies[utt].append(er_count)
		disfluencies[utt].append(hm_count)
		disfluencies[utt].append(pause_count)
		disfluencies[utt].append(repetition_count)
		disfluencies[utt].append(break_count)

	return disfluencies

def total_disfluencies(dpu_dict):
	disfluencies = {}
	disfluencies["UM"] = 0
	disfluencies["UH"] = 0
	disfluencies["AH"] = 0
	disfluencies["ER"] = 0
	disfluencies["HM"] = 0
	disfluencies["Nasal"] = 0
	disfluencies["Non-Nasal"] = 0
	disfluencies["Pause"] = 0
	disfluencies["Break"] = 0
	disfluencies["Repetitions"] = 0
	for (k, v) in dpu_dict.items():
		disfluencies["UM"] += v[0]
		disfluencies["UH"] += v[1]
		disfluencies["AH"] += v[2]
		disfluencies["ER"] += v[3]
		disfluencies["HM"] += v[4]
		disfluencies["Pause"] += v[5]
		disfluencies["Repetitions"] += v[6]
		disfluencies["Break"] += v[7]

	disfluencies["Nasal"] = disfluencies["UM"] + disfluencies["HM"]
	disfluencies["Non-Nasal"] = disfluencies["UH"] + disfluencies["AH"] + disfluencies["ER"]

	return disfluencies
