#!/usr/bin/python

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

class Tagger:
	__tag_dict = {}
	def __init__(self, tag_dict):
		"""
		Creates a Tagger object.
		"""
		raise NotImplementedError

	def tag(self, text):
		"""
		Return a list of tuples where each pair is a word and its TAG
		:param text:a string of text to be tagged
		:type text:str
		:return:a list of tuples where each pair is a word and its TAG
		:rtype:list of tuples
		"""
		raise NotImplementedError

	def untag(self, tagged_list):
		"""
		Return a string of untagged text
		:param tagged_list:a list of tuples where each pair is a word and TAG
		:type tagged_list:list of tuples
		:return:a string of text
		:rtype:str
		"""
		raise NotImplementedError