#!/usr/bin/python3.4

##### PYTHON IMPORTS ###################################################################################################
import sys

##### NLTK IMPORTS #####################################################################################################
from nltk.tree import Tree

##### SPLAT IMPORTS ####################################################################################################
from base.Util import open_class_list, ignore_list, proposition_list

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

def calc_content_density(tagged_text):
	""" Calculate the content density. """
	open_class_count, closed_class_count = 0, 0

	for item in tagged_text:
		if item[1] in open_class_list:
			open_class_count += 1
		elif item[1] not in ignore_list:
			closed_class_count += 1

	return float(open_class_count) / float(closed_class_count)

def calc_idea_density(tagged_text):
	""" Calculate the idea density. """
	proposition_count = 0
	for item in tagged_text:
		if item[1] in proposition_list:
			proposition_count += 1

	return float(proposition_count) / float(len(tagged_text))

# The code contained in this section was adapted based on the code located here:
# https://github.com/neubig/util-scripts/blob/96c91e43b650136bb88bbb087edb1d31b65d389f/syntactic-complexity.py
# Permission was granted by Graham Neubig, the code creator, to use his code. For questions regarding his code,
# he may be contacted by email < neubig@is.naist.jp > or you can visit his website
# http://www.phontron.com/index.php
def get_word_score(tree):
	""" Calculate the word score for each tree. """
	if type(tree) == str:
		return 1
	else:
		score = 0
		for child in tree:
			score += get_word_score(child)
		return score

def is_sentence(value):
	""" Determine if the given string is a sentence. """
	if len(value) > 0 and value[0] == "S":
		return True
	else:
		return False

def calc_yngve_score(tree, parent):
	""" Calculate the Yngve Score for a given input_file. """
	if type(tree) == str:
		return parent
	else:
		count = 0
		for i, child in enumerate(reversed(tree)):
			count += calc_yngve_score(child, parent + i)
		return count

def calc_frazier_score(tree, parent, parent_label):
	""" Calculate the Frazier Score for a given input_file. """
	my_lab = ''
	if type(tree) == str:
		return parent - 1
	else:
		count = 0
		for i, child in enumerate(tree):
			score = 0
			if i == 0:
				my_lab = tree.label()
				if is_sentence(my_lab):
					score = (0 if is_sentence(parent_label) else parent + 1.5)
				elif my_lab != "" and my_lab != "ROOT" and my_lab != "TOP":
					score = parent + 1
			count += calc_frazier_score(child, score, my_lab)
		return count

def get_formatted_trees(treestrings):
	""" Format the parse-tree-strings so they can be fed to the Frazier & Yngve parsers. """
	form_trees = []
	for item in treestrings:
		form_trees.append('( ' + item + ' )')

	return form_trees

def get_yngve_score(treestrings):
	""" Average all of the yngve scores for the given input_file. """
	total_yngve_score = 0
	for tree_line in treestrings:#get_formatted_trees(treestrings):
		if tree_line.strip() == "":
			continue
		tree = Tree.fromstring(tree_line)
		raw_yngve_score = calc_yngve_score(tree, 0)
		try:
			mean_yngve_score = float(raw_yngve_score) / float(get_word_score(tree))
			total_yngve_score += mean_yngve_score
		except ZeroDivisionError:
			print('WARNING: ZeroDivisionError for the tree: ' + str(tree))
			pass

	score = float(total_yngve_score) / float(len(treestrings)) if len(treestrings) != 0 else 0

	return score

def get_frazier_score(treestrings):
	""" Average all of the frazier scores for the given input_file. """
	sentences, total_frazier_score = 0, 0
	for tree_line in treestrings:#get_formatted_trees(treestrings):
		if tree_line.strip() == "":
			continue
		tree = Tree.fromstring(tree_line)
		sentences += 1
		raw_frazier_score = calc_frazier_score(tree, 0, "")
		try:
			mean_frazier_score = float(raw_frazier_score) / float(get_word_score(tree))
			total_frazier_score += mean_frazier_score
		except ZeroDivisionError:
			print('WARNING: ZeroDisvisionError for the tree: ' + str(tree))
			pass

	score = float(total_frazier_score) / float(len(treestrings)) if len(treestrings) != 0 else 0

	return score

# The code below is experimental. It's intention is to calculate Yngve and Frazier scores without the overhead of
# creating NLTK Tree objects and traversing the branches. Instead, it traverses the parenthesis of the treestring.

#TODO TEST THIS
def new_yngve(treestring):
	just_pushed = False
	stack = 0
	total = 0
	child_total = 0
	tree = "(" + treestring + ")"
	for char in tree:
		if char == "(":
			just_pushed = True
			stack += 1
		elif char == ")":
			if just_pushed:
				total += stack
				child_total += 1
			just_pushed = False
			stack -= 1
		else:
			pass

	return float(total) / float(child_total)

def yngve(treestrings):
	individual_scores = 0
	for treestring in treestrings:
		individual_scores += new_yngve(treestring)

	return float(individual_scores) / float(len(treestrings))