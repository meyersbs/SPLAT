#!/usr/bin/python

from base import Sent
from model import NGramminator

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

class TextBubble:
	"""
	A TextBubble is a bubble of text. It can be a single word, a paragraph, or even a whole novel!
	The TextBubble object makes it super simple to extract features from a selection of text.
	"""
	bubble = ""
	sentences = []
	tokens = []
	types = {}
	ngramminator = NGramminator()
	def __init__(self, textbubble):
		if type(textbubble) == str:
			self.bubble = textbubble
			for sentence in textbubble.split("\n"):
				self.sentences.append(Sent(sentence))
			for sentence in self.sentences:
				for word in sentence.words():
					self.tokens.append(word)
			temp_types = {}
			for word in self.tokens:
				if word not in temp_types.keys():
					temp_types[word] = 1
				else:
					temp_types[word] += 1
			self.types = temp_types
		else:
			raise ValueError("textbubble must be of type str")

	def bubble(self):
		"""
		:return:the raw TextBubble
		:rtype:str
		"""
		return self.bubble

	def sents(self):
		"""
		:return:a list of sentences
		:rtype:list
		"""
		return self.sentences

	def tokens(self):
		"""
		:return:a list of tokens
		:rtype:list
		"""
		return self.tokens

	def types(self):
		"""
		:return:a list of types
		:rtype:list
		"""
		return self.types

	def wordcount(self):
		"""
		:return:the total wordcount of the TextBubble
		:rtype:int
		"""
		return len(self.tokens)

	def unique_wordcount(self):
		"""
		:return:the number of types in the TextBubble
		:rtype:int
		"""
		return len(self.types.keys())

	def sentcount(self):
		"""
		:return:the number of sentences in the TextBubble
		:rtype:int
		"""
		return len(self.sentences)

	def type_token_ratio(self):
		"""
		:return:the type-token ratio of the TextBubble
		:rtype:float
		"""
		return round((float((self.unique_wordcount / self.wordcount) * 100), 4))

	def unigrams(self):
		"""
		:return:a list of unigrams
		:rtype:list of tuples
		"""
		return self.ngramminator.unigrams(self.bubble)

	def bigrams(self):
		"""
		:return:a list of bigrams
		:rtype:list of tuples
		"""
		return self.ngramminator.bigrams(self.bubble)

	def trigrams(self):
		"""
		:return:a list of trigrams
		:rtype:list of tuples
		"""
		return self.ngramminator.trigrams(self.bubble)

	def ngrams(self, n):
		"""
		:return:a list of ngrams of size n
		:rtype:list of tuples
		"""
		return self.ngramminator.ngrams(self.bubble, n)

	def splat(self):
		"""
		:return:a massive SPLAT of the different features in the TextBubble
		:rtype:str
		"""
		output = "===== Bubble:\n"
		output += self.bubble + "\n"
		output += "===== Sentences:\n"
		count = 0
		for sentence in self.sentences:
			output += "[" + str(count) + "] " + sentence.string + "\n"
			count += 1
		output += "Sentence Count: " + str(self.sentcount) + "\n"
		output += "===== Tokens:\n"
		output += self.tokens + "\n"
		output += "Word Count: " + str(self.wordcount) + "\n"
		output += "===== Types:\n"
		output += self.types + "\n"
		output += "Unique Word Count: " + str(self.unique_wordcount) + "\n"
		output += "===== Type-Token Ratio:\n"
		output += str(self.type_token_ratio) + "\n"
