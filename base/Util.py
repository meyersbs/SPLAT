#!/usr/bin/python

import re
import os.path

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
punctlist = [".", "!", "?"]

def __tokenize_list(text):
	"""
	Returns a list of tokens.
	:param text:a list of strings to be tokenized
	:type text:list
	:return:a list of tokens
	:rtype:list
	"""
	tokens = []
	for item in text:
		for word in item.split(" "):
			tokens.append(word)

	return tokens

def __tokenize_string(text):
	"""
	Returns a list of tokens.
	:param text:a string to be tokenized
	:type text:str
	:return:a list of tokens
	:rtype:list
	"""
	tokens = []
	for word in text.split(" "):
		tokens.append(word)

	return tokens

def __tokenize_file(text):
	"""
	Returns a list of tokens.
	:param text:a list of strings to be tokenized
	:type text:filename
	:return:a list of tokens
	:rtype:list
	"""
	tokens = []
	with open(text, 'r') as f:
		for line in f:
			for word in line.split(" "):
				tokens.append(word)

	return tokens


def tokenize(text):
	"""
	Determines whether the given text is a string, a list of string, or a valid filename.
	Generates a list of rawtokens and a list of normalized tokens.
	Returns a list with two sublists. Index 0 is the list of rawtokens. Index 1 is the list of normalized tokens.
	:param text:some text to be tokenized
	:type text:str,list,filename
	:return:a list with two items
	:rtype:list of lists
	"""
	output = []
	raw_tokens = []
	clean_tokens = []
	if type(text) == str:
		if os.path.exists(text):
			raw_tokens = __tokenize_file(text)
		else:
			raw_tokens = __tokenize_string(text)
	elif type(text) == list:
		raw_tokens = __tokenize_list(text)
	else:
		raise ValueError("Text to tokenize must be of type str or type list.")

	temp = []
	for token in raw_tokens:
		if token != "" and token != " ":
			temp.append(token.strip("\n"))

	raw_tokens = temp

	output.append(raw_tokens)

	for word in raw_tokens:
		clean_word = re.sub(r"[\.,!\?]", "", word)
		clean_tokens.append(clean_word.lower())

	output.append(clean_tokens)

	return output

def __sentenize_list(text):
	"""
	Returns a list of sentences.
	:param text:a list of strings to be sentenized
	:type text:list
	:return:list of sentences
	:rtype:list
	"""
	global punctlist
	sentences = []
	for item in text:
		temp_sent = ""
		for word in item.split(" "):
			punct_flag = False
			for punct in punctlist:
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

def __sentenize_string(text):
	"""
	Returns a list of sentences.
	:param text:a string to be sentenized
	:type text:str
	:return:list of sentences
	:rtype:list
	"""
	global punctlist
	sentences = []
	temp_sent = ""
	for word in text.split(" "):
		punct_flag = False
		for punct in punctlist:
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

def __sentenize_file(text):
	"""
	Returns a list of sentences.
	:param text:a file to be sentenized
	:type text:filename
	:return:list of sentences
	:rtype:list
	"""
	global punctlist
	sentences = []
	temp_sent = ""
	with open(text, 'r') as f:
		for line in f:
			for word in line.split(" "):
				punct_flag = False
				for punct in punctlist:
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

def sentenize(text):
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
			sentences = __sentenize_file(text)
		else:
			sentences = __sentenize_string(text)
	elif type(text) == list:
		sentences = __sentenize_list(text)
	else:
		raise ValueError("Text to sentenize must be of type str or type list.")

	temp = []
	for sent in sentences:
		temp.append(re.sub(r"\n", "", sent))

	sentences = temp

	return sentences

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