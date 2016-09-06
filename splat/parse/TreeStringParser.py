#!/usr/bin/env python3

##### PYTHON IMPORTS ###################################################################################################
import subprocess, os

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

class TreeStringParser:
	curr_dir = os.path.dirname(__file__)
	__berkeley_path = ""
	__grammar_path = ""
	def __init__(self, berkeley_path=curr_dir + '/BerkeleyParser-1.7.jar', grammar_path=curr_dir + '/eng_sm6.gr'):
		self.__berkeley_path = berkeley_path
		self.__grammar_path = grammar_path

	def get_parse_trees(self, sentences):
		""" Use the Berkeley Parser to obtain parse-tree-strings for each line in the input_file. """
		parse_file = open("parse_file.txt", 'w')
		for sentence in sentences:
			parse_file.write(sentence + "\n")
		parse_file.close()

		rawtrees = subprocess.Popen(['java', '-jar', self.__berkeley_path, '-gr', self.__grammar_path, '-inputFile', parse_file.name, '-nThreads', '1'], stdout=subprocess.PIPE).communicate()[0]
		temp_parse_trees = rawtrees.decode("utf-8").split("\n")

		parse_trees = []
		for tree in temp_parse_trees:
			if tree != "":
				parse_trees.append(tree)

		os.remove(parse_file.name)
		return parse_trees
