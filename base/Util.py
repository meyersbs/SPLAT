#!/usr/bin/python

from corpus.Util import Stopwords
from nltk.tree import Tree

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
