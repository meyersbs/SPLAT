#!/usr/bin/env python3

##### NLTK IMPORTS #####################################################################################################
from nltk import pos_tag
from nltk import word_tokenize

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

class NLTKPOSTagger:
	"""
	An NLTKPOSTagger tokenizes the given input with punctuation as separate tokens, and then does a dictionary lookup to
	determine the part-of-speech for each token.
	"""

	def __init__(self):
		"""
		Creates a Tagger object.
		"""
		pass

	def tag(self, text):
		"""
		Return a list of tuples where each pair is a word and its TAG
		:param text:a string of text to be tagged
		:type text:
		:return:a list of tuples where each pair is a word and its TAG
		:rtype:list of tuples
		"""
		tagged_text = []
		if type(text) == str:
			tagged_text = pos_tag(word_tokenize(text))
		elif type(text) == list:
			new_text = " ".join(text)
			tagged_text = pos_tag(word_tokenize(new_text))

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

	def dump(self, out_file):
		json.dump(self.__dict__, out_file, default=jdefault)

	def dumps(self):
		return json.dumps(self.__dict__)

	def load(self, in_file):
		self.__dict__ = json.load(in_file)

	def loads(self, data_str):
		self.__dict__ = json.loads(data_str)

def jdefault(o):
	return o.__dict__
