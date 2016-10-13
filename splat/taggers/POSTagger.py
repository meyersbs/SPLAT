#!/usr/bin/env python3

##### SPLAT IMPORTS ####################################################################################################
from splat.corpora.Util import Brown
from tokenizers.PunctTokenizer import PunctTokenizer

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

class POSTagger:
	"""
	A POSTagger tokenizes the given input with punctuation as separate tokens, and then does a dictionary lookup to
	determine the part-of-speech for each token.
	"""
	__tags_dict = {}
	__p_tokenizer = PunctTokenizer()

	def __init__(self, tag_dict=Brown, tokenizer=PunctTokenizer()):
		"""
		Creates a Tagger object.
		"""
		self.__tags_dict = tag_dict
		self.__p_tokenizer = tokenizer

	def __tag_list(self, text_list):
		tagged = []
		for word in self.__p_tokenizer.tokenize(text_list):
			if word.lower() in self.__tags_dict.keys():
				tag = self.__tags_dict[word.lower()]
			elif word in [".", ",", ":", ";", "?", "!"]:
				tag = u"PNCT"
			else:
				tag = u"UNK"
			tagged.append((word, tag))

		return tagged

	def __tag_str(self, text_str):
		tagged = []
		for word in self.__p_tokenizer.tokenize(text_str):
			if word in self.__tags_dict.keys():
				tag = self.__tags_dict[word]
			elif word == "." or word == "!" or word == "?" or word == "," or word == ":" or word == ";":
				tag = u"PNCT"
			else:
				tag = u"UNK"
			tagged.append((word, tag))

		return tagged

	def tag(self, text):
		"""
		Return a list of tuples where each pair is a word and its TAG
		:param text:a string of text to be tagged
		:type text:
		:return:a list of tuples where each pair is a word and its TAG
		:rtype:list of tuples
		"""
		tagged_text = []
		if type(text) == list:
			tagged_text = self.__tag_list(text)
		elif type(text) == str:
			tagged_text = self.__tag_str(text)

		return tagged_text


	def untag(self, tagged_list):
		"""
		Return a string of untagged text
		:param tagged_list:a list of tuples where each pair is a word and TAG
		:type tagged_list:list of tuples
		:return:a string of text
		:rtype:str
		"""
		raise NotImplementedError