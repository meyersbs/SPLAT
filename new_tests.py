#!/usr/bin/python3.4

##### PYTHON IMPORTS ###################################################################################################
import unittest

##### SPLAT IMPORTS ####################################################################################################
from splat.base.TextBubble import TextBubble

##### GLOBAL VARIABLES #################################################################################################


class TestBasics(unittest.TestCase):
	whitman_bubble = TextBubble("tests/whitman_test.txt")
	frankenstein_bubble = TextBubble("tests/frankenstein_test.txt")
	flesch_bubble = TextBubble("tests/flesch_kincaid_test.txt")

	def test_sents(self):
		expected = ['I celebrate myself, and sing myself, And what I assume you shall assume, For every atom belonging to me as good belongs to you.']
		output = self.whitman_bubble.sents()
		unexpected = self.frankenstein_bubble.sents()
		self.assertEqual(output, expected)
		self.assertNotEqual(output, unexpected)

	def test_sentcount(self):
		expected = 2
		output = self.frankenstein_bubble.sentcount()
		unexpected = self.whitman_bubble.sentcount()
		self.assertEqual(output, expected)
		self.assertNotEqual(output, unexpected)

	def test_utts(self):
		expected = ['I celebrate myself, and sing myself,', 'And what I assume you shall assume,', 'For every atom belonging to me as good belongs to you.']
		output = self.whitman_bubble.utts()
		unexpected = self.frankenstein_bubble.utts()
		self.assertEqual(output, expected)
		self.assertNotEqual(output, unexpected)

	def test_uttcount(self):
		expected = 3
		output = self.frankenstein_bubble.uttcount()
		unexpected = self.flesch_bubble.uttcount()
		self.assertEqual(output, expected)
		self.assertNotEqual(output, unexpected)

	def test_tokens(self):
		expected = ['i', 'celebrate', 'myself', 'and', 'sing', 'myself', 'and', 'what', 'i', 'assume', 'you', 'shall', 'assume', 'for', 'every', 'atom', 'belonging', 'to', 'me', 'as', 'good', 'belongs', 'to', 'you']
		output = self.whitman_bubble.tokens()
		unexpected = self.frankenstein_bubble.tokens()
		self.assertEqual(output, expected)
		self.assertNotEqual(output, unexpected)

	def test_types(self):
		expected = [('and', 2), ('as', 1), ('assume', 2), ('atom', 1), ('belonging', 1), ('belongs', 1), ('celebrate', 1), ('every', 1), ('for', 1), ('good', 1), ('i', 2), ('me', 1), ('myself', 2), ('shall', 1), ('sing', 1), ('to', 2), ('what', 1), ('you', 2)]
		output = self.whitman_bubble.types()
		unexpected = self.frankenstein_bubble.types()
		self.assertEqual(output, expected)
		self.assertNotEqual(output, unexpected)

	def test_type_token_ratio(self):
		expected = 81.6327
		output = self.frankenstein_bubble.type_token_ratio()
		unexpected = self.whitman_bubble.type_token_ratio()
		self.assertEqual(output, expected)
		self.assertNotEqual(output, unexpected)

	def test_syllables(self):
		expected = 26
		output = self.flesch_bubble.syllables()
		acceptable_range = [25, 26, 27]
		self.assertTrue(output in acceptable_range)
		self.assertNotEqual(output, expected)

	def test_wordcount(self):
		expected = 49
		output = self.frankenstein_bubble.wordcount()
		unexpected = self.whitman_bubble.wordcount()
		self.assertEqual(output, expected)
		self.assertNotEqual(output, unexpected)

	def test_unique_wordcount(self):
		expected = 18
		output = self.whitman_bubble.unique_wordcount()
		unexpected = self.frankenstein_bubble.unique_wordcount()
		self.assertEqual(output, expected)
		self.assertNotEqual(output, unexpected)

	def test_content_words(self):
		expected = ['rejoice', 'hear', 'disaster', 'accompanied', 'commencement', 'enterprise', 'regarded', 'evil', 'forebodings', 'arrived', 'yesterday', 'first', 'task', 'assure', 'dear', 'sister', 'welfare', 'increasing', 'confidence', 'success', 'undertaking']
		output = self.frankenstein_bubble.content_words()
		unexpected = self.whitman_bubble.content_words()
		self.assertEqual(output, expected)
		self.assertNotEqual(output, unexpected)

	def test_function_words(self):
		expected = ['you', 'will', 'to', 'that', 'no', 'has', 'the', 'of', 'an', 'which', 'you', 'have', 'with', 'such', 'i', 'here', 'and', 'my', 'is', 'to', 'my', 'of', 'my', 'and', 'in', 'the', 'of', 'my']
		output = self.frankenstein_bubble.function_words()
		unexpected = self.whitman_bubble.function_words()
		self.assertEqual(output, expected)
		self.assertNotEqual(output, unexpected)

	def test_content_function_ratio(self):
		expected = 0.75
		output = self.frankenstein_bubble.content_function_ratio()
		unexpected = self.whitman_bubble.content_function_ratio()
		self.assertEqual(output, expected)
		self.assertNotEqual(output, unexpected)

	def test_unique_content_words(self):
		expected = ['assume', 'atom', 'belonging', 'belongs', 'celebrate', 'every', 'good', 'shall', 'sing']
		output = self.whitman_bubble.unique_content_words()
		unexpected = self.frankenstein_bubble.unique_content_words()
		self.assertEqual(output, expected)
		self.assertNotEqual(output, unexpected)

	def test_unique_function_words(self):
		expected = ['and', 'as', 'for', 'i', 'me', 'myself', 'to', 'what', 'you']
		output = self.whitman_bubble.unique_function_words()
		unexpected = self.frankenstein_bubble.unique_function_words()
		self.assertEqual(output, expected)
		self.assertNotEqual(output, unexpected)

class TestComplexity(unittest.TestCase):
	whitman_bubble = TextBubble("tests/whitman_test.txt")
	frankenstein_bubble = TextBubble("tests/frankenstein_test.txt")
	flesch_bubble = TextBubble("tests/flesch_kincaid_test.txt")

	def test_idea_density(self):
		expected = 0.5
		output = self.whitman_bubble.idea_density()
		unexpected = self.frankenstein_bubble.idea_density()
		self.assertEqual(output, expected)
		self.assertNotEqual(output, unexpected)

	def test_content_density(self):
		expected = 0.4
		output = self.whitman_bubble.content_density()
		unexpected = self.frankenstein_bubble.content_density()
		self.assertEqual(output, expected)
		self.assertNotEqual(output, unexpected)

if __name__ == '__main__':
	unittest.main()
