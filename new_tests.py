#!/usr/bin/python3

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
		expected = 0.8163
		output = self.frankenstein_bubble.type_token_ratio()
		unexpected = self.whitman_bubble.type_token_ratio()
		self.assertEqual(output, expected)
		self.assertNotEqual(output, unexpected)

	def test_syllables(self):
		expected = 26
		output = self.flesch_bubble.syllables()
		self.assertEqual(output, expected)

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

class TestParsing(unittest.TestCase):

	def test_garden_path(self):
		pass

	def test_local_ambiguity(self):
		pass

	def test_global_ambiguity(self):
		pass

class TestComplexity(unittest.TestCase):
	whitman_bubble = TextBubble("tests/whitman_test.txt")
	frankenstein_bubble = TextBubble("tests/frankenstein_test.txt")
	flesch_bubble = TextBubble("tests/flesch_kincaid_test.txt")
	roark_bubble = TextBubble("tests/roark_sample.txt")

	def test_idea_density(self):
		expected = 0.5833
		output = self.whitman_bubble.idea_density()
		unexpected = self.frankenstein_bubble.idea_density()
		self.assertAlmostEqual(output, expected, 3)
		self.assertNotEqual(output, unexpected)

	def test_content_density(self):
		expected = 0.5
		output = self.whitman_bubble.content_density()
		unexpected = self.frankenstein_bubble.content_density()
		self.assertAlmostEqual(output, expected, 3)
		self.assertNotEqual(output, unexpected)

	def test_tree_based_yngve(self):
		expected = 1.1250
		output = self.roark_bubble.tree_based_yngve_score()
		unexpected = self.whitman_bubble.tree_based_yngve_score()
		self.assertEqual(output, expected)
		self.assertNotEqual(output, unexpected)

	def test_tree_based_frazier(self):
		expected = 0.9375
		output = self.roark_bubble.tree_based_frazier_score()
		unexpected = self.whitman_bubble.tree_based_frazier_score()
		self.assertEqual(output, expected)
		self.assertNotEqual(output, unexpected)

	def test_flesch_readability(self):
		expected = 24.4
		output = self.flesch_bubble.flesch_readability()
		unexpected = self.whitman_bubble.flesch_readability()
		self.assertAlmostEqual(output, expected, 1)
		self.assertNotEqual(output, unexpected)

	def test_flesch_kincaid(self):
		expected = 13.1
		output = self.flesch_bubble.kincaid_grade_level()
		unexpected = self.whitman_bubble.kincaid_grade_level()
		self.assertEqual(output, expected)
		self.assertNotEqual(output, unexpected)

class TestSyllables(unittest.TestCase):

	def test_suffixes(self):
		expected_added = 2
		output_added = TextBubble("added").syllables()
		self.assertEqual(output_added, expected_added)
		expected_apples = 2
		output_apples = TextBubble("apples").syllables()
		self.assertEqual(output_apples, expected_apples)
		expected_foxes = 2
		output_foxes = TextBubble("foxes").syllables()
		self.assertEqual(output_foxes, expected_foxes)
		expected_auntie = 2
		output_auntie = TextBubble("auntie").syllables()
		self.assertEqual(output_auntie, expected_auntie)

	def test_syllabic_l(self):
		expected_mantle = 2
		output_mantle = TextBubble("mantle").syllables()
		self.assertEqual(output_mantle, expected_mantle)
		expected_bottle = 2
		output_bottle = TextBubble("bottle").syllables()
		self.assertEqual(output_bottle, expected_bottle)
		expected_saddle = 2
		output_saddle = TextBubble("saddle").syllables()
		self.assertEqual(output_saddle, expected_saddle)
		expected_poodle = 2
		output_poodle = TextBubble("poodle").syllables()
		self.assertEqual(output_poodle, expected_poodle)
		expected_pistol = 2
		output_pistol = TextBubble("pistol").syllables()
		self.assertEqual(output_pistol, expected_pistol)
		expected_tunnel = 2
		output_tunnel = TextBubble("tunnel").syllables()
		self.assertEqual(output_tunnel, expected_tunnel)

	def test_syllabic_m(self):
		expected_heroism = 4
		output_heroism = TextBubble("heroism").syllables()
		self.assertEqual(output_heroism, expected_heroism)
		expected_feudalism = 4
		output_feudalism = TextBubble("feudalism").syllables()
		self.assertEqual(output_feudalism, expected_feudalism)
		expected_blossom = 2
		output_blossom = TextBubble("blossom").syllables()
		self.assertEqual(output_blossom, expected_blossom)
		expected_rhythm = 2
		output_rhythm = TextBubble("rhythm").syllables()
		self.assertEqual(output_rhythm, expected_rhythm)

	def test_syllabic_n(self):
		expected_cotton = 2
		output_cotton = TextBubble("cotton").syllables()
		self.assertEqual(output_cotton, expected_cotton)
		expected_button = 2
		output_button = TextBubble("button").syllables()
		self.assertEqual(output_button, expected_button)
		expected_risen = 2
		output_risen = TextBubble("risen").syllables()
		self.assertEqual(output_risen, expected_risen)
		expected_prison = 2
		output_prison = TextBubble("prison").syllables()
		self.assertEqual(output_prison, expected_prison)
		expected_sadden = 2
		output_sadden = TextBubble("sadden").syllables()
		self.assertEqual(output_sadden, expected_sadden)
		expected_listen = 2
		output_listen = TextBubble("listen").syllables()
		self.assertEqual(output_listen, expected_listen)

	def test_syllabic_ng(self):
		expected_going = 2
		output_going = TextBubble("going").syllables()
		self.assertEqual(output_going, expected_going)
		expected_listening = 3
		output_listening = TextBubble("listening").syllables()
		self.assertEqual(output_listening, expected_listening)
		expected_ringing = 2
		output_ringing = TextBubble("ringing").syllables()
		self.assertEqual(output_ringing, expected_ringing)

	def test_syllabic_r(self):
		expected_history = 3
		output_history = TextBubble("history").syllables()
		self.assertEqual(output_history, expected_history)
		expected_hungary = 3
		output_hungary = TextBubble("hungary").syllables()
		self.assertEqual(output_hungary, expected_hungary)
		expected_preference = 3
		output_preference = TextBubble("preference").syllables()
		self.assertEqual(output_preference, expected_preference)

	def test_special_cases(self):
		expected_australian = 4
		output_australian = TextBubble("australian").syllables()
		self.assertEqual(output_australian, expected_australian)
		expected_literal = 3
		output_literal = TextBubble("literal").syllables()
		self.assertEqual(output_literal, expected_literal)
		expected_forebodings = 4
		output_forebodings = TextBubble("forebodings").syllables()
		self.assertEqual(output_forebodings, expected_forebodings)
		expected_pterodactyl = 4
		output_pterodactyl = TextBubble("pterodactyl").syllables()
		self.assertEqual(output_pterodactyl, expected_pterodactyl)

	def test_proper_names(self):
		expected_benjamin = 3
		output_benjamin = TextBubble("benjamin").syllables()
		self.assertEqual(output_benjamin, expected_benjamin)
		expected_emily = 3
		output_emily = TextBubble("emily").syllables()
		self.assertEqual(output_emily, expected_emily)
		expected_cissi = 2
		output_cissi = TextBubble("cissi").syllables()
		self.assertEqual(output_cissi, expected_cissi)
		expected_cecilia = 4
		output_cecilia = TextBubble("cecilia").syllables()
		self.assertEqual(output_cecilia, expected_cecilia)
		expected_ares = 2
		output_ares = TextBubble("ares").syllables()
		self.assertEqual(output_ares, expected_ares)

if __name__ == '__main__':
	unittest.main()
