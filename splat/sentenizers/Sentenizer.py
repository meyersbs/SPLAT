#!/usr/bin/env python3

##### SPLAT IMPORTS ####################################################################################################
import os.path

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

class Sentenizer:
	"""
	A Sentenizer provides the functionality to generate a list of sentences from a text input.
	"""
	punctlist = [".", "!", "?"]

	def __init__(self):
		"""
		Creates a Sentenizer object.
		"""
		pass

	@staticmethod
	def __sentenize_list(self, text):
		"""
		Returns a list of sentences.
		:param text:a list of strings to be sentenized
		:type text:list
		:return:list of sentences
		:rtype:list
		"""
		sentences = []
		for item in text:
			temp_sent = ""
			for word in item.split(" "):
				punct_flag = False
				for punct in self.punctlist:
					if punct in word:
						punct_flag = True
						break
				if punct_flag:
					temp_sent += word
					sentences.append(temp_sent)
					temp_sent = ""
				else:
					temp_sent += word + " "

		return sentences

	@staticmethod
	def __sentenize_string(self, text):
		"""
		Returns a list of sentences.
		:param text:a string to be sentenized
		:type text:str
		:return:list of sentences
		:rtype:list
		"""
		sentences = []
		temp_sent = ""
		for word in text.split(" "):
			punct_flag = False
			for punct in self.punctlist:
				if punct in word:
					punct_flag = True
					break
			if punct_flag:
				temp_sent += word
				sentences.append(temp_sent)
				temp_sent = ""
			else:
				temp_sent += word + " "

		return sentences

	@staticmethod
	def __sentenize_file(self, text):
		"""
		Returns a list of sentences.
		:param text:a file to be sentenized
		:type text:filename
		:return:list of sentences
		:rtype:list
		"""
		sentences = []
		temp_sent = ""
		with open(text, 'r') as f:
			for line in f:
				for word in line.split(" "):
					punct_flag = False
					for punct in self.punctlist:
						if punct in word:
							punct_flag = True
							break
					if punct_flag:
						temp_sent += word
						sentences.append(temp_sent)
						temp_sent = ""
					else:
						temp_sent += word + " "

		return sentences

	def sentenize(self, text):
		"""
		Determines whether the given text is a string, a list of string, or a valid filename.
		Generates a list of sentences.
		:param text:some text to be tokenized
		:type text:str,list,filename
		:return:list of sentences
		:rtype:list
		"""
		sentences = []
		if type(text) == str:
			if os.path.exists(text):
				sentences = self.__sentenize_file(self, text)
			else:
				sentences = self.__sentenize_string(self, text)
		elif type(text) == list:
			sentences = self.__sentenize_list(self, text)
		else:
			raise ValueError("Text to sentenize must be of type str or type list.")

		return sentences