#!/usr/bin/python3.4

##### PYTHON IMPORTS ###################################################################################################
import unittest

##### SPLAT IMPORTS ####################################################################################################
from splat.base.TextBubble import TextBubble

##### GLOBAL VARIABLES #################################################################################################


class TestBasics(unittest.TestCase):
	whitman_bubble = TextBubble("tests/whitman_test.txt")
	frankenstein_bubble = TextBubble("tests/frankenstein_test.txt")

	def test_sents(self):
		expected = ['I celebrate myself, and sing myself, And what I assume you shall assume, For every atom belonging to me as good belongs to you.']
		output = self.whitman_bubble.sents()
		self.assertEqual(output, expected)

	def test_sentcount(self):
		expected = 2
		output = self.frankenstein_bubble.sentcount()
		self.assertEqual(output, expected)

	def test_utts(self):
		expected = ['I celebrate myself, and sing myself,', 'And what I assume you shall assume,', 'For every atom belonging to me as good belongs to you.']
		output = self.whitman_bubble.utts()
		self.assertEqual(output, expected)

	def test_tokens(self):
		expected = ['i', 'celebrate', 'myself', 'and', 'sing', 'myself', 'and', 'what', 'i', 'assume', 'you', 'shall', 'assume', 'for', 'every', 'atom', 'belonging', 'to', 'me', 'as', 'good', 'belongs', 'to', 'you']
		output = self.whitman_bubble.tokens()
		self.assertEqual(output, expected)

	def test_types(self):
		pass

if __name__ == '__main__':
	unittest.main()
