#!/usr/bin/python3.4

##### PYTHON IMPORTS ###################################################################################################
import sys, re

##### NLTK IMPORTS #####################################################################################################
from nltk.tree import Tree

##### SPLAT IMPORTS ####################################################################################################
from splat.base.Util import open_class_list, ignore_list, proposition_list

########################################################################################################################
##### INFORMATION ######################################################################################################
### @PROJECT_NAME:		SPLAT: Speech Processing and Linguistic Annotation Tool										 ###
### @VERSION_NUMBER:																								 ###
### @PROJECT_SITE:		github.com/meyersbs/SPLAT																     ###
### @AUTHOR_NAME:		Benjamin S. Meyers																			 ###
### @CONTACT_EMAIL:		ben@splat-library.org																				 ###
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

	return float(open_class_count) / float(closed_class_count) if float(closed_class_count) != 0 else 0

def calc_idea_density(tagged_text):
	""" Calculate the idea density. """
	proposition_count = 0
	for item in tagged_text:
		if item[1] in proposition_list:
			proposition_count += 1

	return float(proposition_count) / float(len(tagged_text)) if float(len(tagged_text)) != 0 else 0

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

def yngve_redux(treestring):
	""" For the given parse-tree-string, return the word count and the yngve score. """
	tree = Tree.fromstring(treestring)
	total = float(calc_yngve_score(tree, 0))
	words = float(get_word_score(tree))

	return [total, words]

def yngve_redux(treestring):
	""" For the given parse-tree-string, return the word count and the yngve score. """
	tree = Tree.fromstring(treestring)
	total = float(calc_yngve_score(tree, 0))
	words = float(get_word_score(tree))

	return [total, words]

def get_mean_yngve(treestrings):
	""" Average all of the yngve scores for the given input_file. """
	count = 0
	total = 0
	for treestring in treestrings:
		results = yngve_redux(treestring)
		total += results[0]
		count += results[1]
	return float(total / count)

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

def get_frazier_score(treestrings):
	""" Average all of the frazier scores for the given input_file. """
	sentences, total_frazier_score, total_word_count = 0, 0, 0
	for tree_line in treestrings:
		if tree_line.strip() == "":
			continue
		tree = Tree.fromstring(tree_line)
		sentences += 1
		raw_frazier_score = calc_frazier_score(tree, 0, "")
		try:
			total_word_count += get_word_score(tree)
			total_frazier_score += raw_frazier_score
		except ZeroDivisionError:
			print('WARNING: ZeroDisvisionError for the tree: ' + str(tree))
			pass

	score = float(total_frazier_score) / float(total_word_count)

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

############################
def get_reversed_parentree(parentree):
	reversed_parentree = ""
	for char in reversed(parentree):
		if char == ")":
			reversed_parentree += "("
		elif char == "(":
			reversed_parentree += ")"
		else:
			pass
	return reversed_parentree

def find_sub_parentree(reversed_parentree, start_index):
	count = 0
	end_index = start_index
	for char in reversed_parentree:
		if char == "(":
			count += 1
		else:
			count -= 1
		end_index += 1
		if count == 0:
			break

	return end_index

def calc_score(value, reversed_parentree):
	#print(reversed_parentree)
	reversed_parentree = reversed_parentree[1:-1] # Strip first and last parens
	#print(reversed_parentree)
	START_INDEX = 0
	counter = 0
	total = 0
	print(reversed_parentree)
	print("LEN: " + str(len(reversed_parentree)))
	if len(reversed_parentree) == 2:
		print("HIT: " + str(value))
		return value
	elif len(reversed_parentree) == 0:
		return value
	else:
		while len(reversed_parentree) > 0:
			# Eliminated odd end_index by changing 'counter' to 'START_INDEX'
			end_index = find_sub_parentree(reversed_parentree, START_INDEX)
			print("END: " + str(end_index))
			#if end_index > len(reversed_parentree):
			#	break
			#else:
			if end_index > 0 or end_index <= len(reversed_parentree): # IF EXISTS
				sub_parentree = reversed_parentree[START_INDEX:end_index]
				print("SUB: " + sub_parentree)
				reversed_parentree = reversed_parentree[end_index:]
				print("REM: " + reversed_parentree)
				print("VAL: " + str(value))
				total += value + calc_score(counter, sub_parentree)
				print("TOT: " + str(total))
				#print(counter)
			counter += 1

	return total

def get_single_mean_yngve(treestring):
	#print(treestring)
	reversed_parentree = get_reversed_parentree(treestring)
	#print(reversed_parentree)
	wordcount = len(re.findall(r'\(\)', reversed_parentree))
	#print(wordcount)
	return [calc_score(0, reversed_parentree), wordcount]

def get_total_mean_yngve(treestrings):
	count = 0
	total = 0
	for treestring in treestrings:
		results = get_single_mean_yngve(treestring)
		print(results)
		total += results[0]
		count += results[1]

	return float(total / count)
