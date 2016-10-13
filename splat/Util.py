#!/usr/bin/env python3

##### PYTHON IMPORTS ###################################################################################################
import re

##### NLTK IMPORTS #####################################################################################################
from nltk.tree import Tree
from nltk.probability import FreqDist
from nltk.corpus import stopwords

##### GLOBAL VARIABLES #################################################################################################
open_class_list = ['NN', 'NNS', 'NNP', 'NNPS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS', 'FW']
ignore_list = [ 'LCB', '-LCB-', 'LRB', '-LRB-', 'LS', 'LSB', '-LSB-', '-RRB-', 'RCB', '-RCB-', 'RSB', '-RSB-', 'SYM', 'UH', '$', '``', '"', '\'\'', '(', ')', '()', '( )', ',', '--', '.', ':', 'SBAR', 'SBARQ']
preposition_list = ['CC', 'CD', 'DT', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS', 'IN', 'CC', 'PDT', 'POS', 'PP$', 'PRP$', 'TO', 'WDT', 'WP', 'WPS', 'WRB']
Stopwords = stopwords.words('english')

########################################################################################################################
##### INFORMATION ######################################################################################################
### @PROJECT_NAME:		SPLAT: Speech Processing and Linguistic Analysis Tool										 ###
### @VERSION_NUMBER:																								 ###
### @PROJECT_SITE:		github.com/meyersbs/SPLAT																     ###
### @AUTHOR_NAME:		Benjamin S. Meyers																			 ###
### @CONTACT_EMAIL:		ben@splat-library.org																		 ###
### @LICENSE_TYPE:		MIT																							 ###
########################################################################################################################
########################################################################################################################

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
	""" Return the number of words in the given text. """
	if type(text) == str:
		return len(text.split(" "))
	elif type(text) == list:
		return len(text)
	else:
		raise ValueError("Text to count words for must be of type str or of type list.")

def type_token_ratio(types, tokens):
	""" Calculate the ratio of types to tokens. """
	return round(float(len(types)) / float(len(tokens)), 4)

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

def get_content_function_ratio(content, function):
	""" Calculate the content-function word ratio. """
	ratio = float(len(content)) / float(len(function)) if len(function) != 0 else 0

	return round(ratio, 4)

def draw_trees(treestrings):
	""" Draws pictures of each parsers-tree-string using Matplotlib. """
	for tree_string in treestrings:
		print(tree_string)
		sentence = Tree.fromstring(tree_string)
		sentence.draw()

	return ''

def get_pos_counts(tagged_text):
	""" Calculate the total number of types for each part of speech taggers. """
	pos_counts = {}
	for item in tagged_text:
		if item[1] in pos_counts.keys():
			pos_counts[item[1]] += 1
		else:
			pos_counts.update({item[1]: 1})

	return pos_counts

def get_max_depth(treestrings):
	""" Calculate the max depths for each parsers tree. """
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
	""" Gather disfluency counts per utterance. """
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
		words = 0
		last_word = ""
		for word in utt.split(" "):
			words += 1
			if word.lower() == "um":
				um_count += 1
			elif word.lower() == "uh":
				uh_count += 1
			elif word.lower() == "ah":
				ah_count += 1
			elif word.lower() == "er":
				er_count += 1
			elif word.lower() == "hm":
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
		disfluencies[utt].append(words)

		average_disfluencies = um_count + uh_count + ah_count + er_count + hm_count + pause_count + repetition_count + break_count
		average_disfluencies = float(average_disfluencies / len(utterances))

	return disfluencies, average_disfluencies

def total_disfluencies(dpu_dict):
	""" Gather disfluency counts for the whole SPLAT. """
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

def get_disfluencies_per_act(text):
	""" Gather disfluency counts per dialog act. """
	temp_dpa = {"Info-Request":[0,0,0,0,0,0,0,0], 			"Action-Request":[0,0,0,0,0,0,0,0],
				"Action-Suggest":[0,0,0,0,0,0,0,0], 		"Answer-Yes":[0,0,0,0,0,0,0,0],
				"Answer-No":[0,0,0,0,0,0,0,0], 				"Answer-Neutral":[0,0,0,0,0,0,0,0],
				"Apology":[0,0,0,0,0,0,0,0], 				"Thanks":[0,0,0,0,0,0,0,0],
				"Clarification-Request":[0,0,0,0,0,0,0,0], 	"Acknowledgement":[0,0,0,0,0,0,0,0],
				"Filler":[0,0,0,0,0,0,0,0], 				"Inform":[0,0,0,0,0,0,0,0],
				"Other":[0,0,0,0,0,0,0,0]}
	for line in text.split("\n"):
		#print(line.split("("))
		split_line = line.split("(")
		if len(split_line) >= 2:
			text = line.split("(")[0]
			acts = line.split("(")[1].strip(")").split(", ")
			last_word = ""
			for word in text.split(" "):
				if word.lower() == "um":
					for act in acts:
						temp_dpa[act][0] += 1
				elif word.lower() == "uh":
					for act in acts:
						temp_dpa[act][1] += 1
				elif word.lower() == "ah":
					for act in acts:
						temp_dpa[act][2] += 1
				elif word.lower() == "er":
					for act in acts:
						temp_dpa[act][3] += 1
				elif word.lower() == "hm":
					for act in acts:
						temp_dpa[act][4] += 1
				elif word.lower() == "{sl}":
					for act in acts:
						temp_dpa[act][5] += 1
				elif re.match(r"\-", word):
					for act in acts:
						temp_dpa[act][7] += 1
				elif word == last_word:
					for act in acts:
						temp_dpa[act][6] += 1
				last_word = word

	return temp_dpa
