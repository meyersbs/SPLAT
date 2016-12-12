#!/usr/bin/env python3

##### PYTHON IMPORTS ###################################################################################################
import unittest, sys

##### SPLAT IMPORTS ####################################################################################################
from splat.SPLAT import SPLAT

class TestBasics(unittest.TestCase):
    whitman_splat = SPLAT("tests/whitman_test.txt")
    frankenstein_splat = SPLAT("tests/frankenstein_test.txt")
    flesch_splat = SPLAT("tests/flesch_kincaid_test.txt")

    def test_bad_input(self):
        try:
            dummy_splat = SPLAT([])
        except ValueError as e:
            self.assertEqual(e.args[0], "WARNING: SPLAT must be of type str or file.")
        except TypeError as e:
            self.assertEqual(e.args[0], "argument should be string, bytes or integer, not list")

    def test_sents(self):
        expected = ['I celebrate myself, and sing myself, And what I assume you shall assume, For every atom belonging to me as good belongs to you.']
        output = self.whitman_splat.sents()
        unexpected = self.frankenstein_splat.sents()
        self.assertEqual(output, expected)
        self.assertNotEqual(output, unexpected)

    def test_sentcount(self):
        expected = 2
        output = self.frankenstein_splat.sentcount()
        unexpected = self.whitman_splat.sentcount()
        self.assertEqual(output, expected)
        self.assertNotEqual(output, unexpected)

    def test_utts(self):
        expected = ['I celebrate myself, and sing myself,', 'And what I assume you shall assume,', 'For every atom belonging to me as good belongs to you.']
        output = self.whitman_splat.utts()
        unexpected = self.frankenstein_splat.utts()
        self.assertEqual(output, expected)
        self.assertNotEqual(output, unexpected)

    def test_uttcount(self):
        expected = 3
        output = self.frankenstein_splat.uttcount()
        unexpected = self.flesch_splat.uttcount()
        self.assertEqual(output, expected)
        self.assertNotEqual(output, unexpected)

    def test_tokens(self):
        expected = ['i', 'celebrate', 'myself', 'and', 'sing', 'myself', 'and', 'what', 'i', 'assume', 'you', 'shall', 'assume', 'for', 'every', 'atom', 'belonging', 'to', 'me', 'as', 'good', 'belongs', 'to', 'you']
        output = self.whitman_splat.tokens()
        unexpected = self.frankenstein_splat.tokens()
        self.assertEqual(output, expected)
        self.assertNotEqual(output, unexpected)

    def test_rawtokens(self):
        expected = ['I', 'celebrate', 'myself,', 'and', 'sing', 'myself,', 'And', 'what', 'I', 'assume', 'you', 'shall', 'assume,', 'For', 'every', 'atom', 'belonging', 'to', 'me', 'as', 'good', 'belongs', 'to', 'you.']
        output = self.whitman_splat.rawtokens()
        unexpected = self.whitman_splat.tokens()
        self.assertEqual(output, expected)
        self.assertNotEqual(output, unexpected)

    def test_types(self):
        expected = [('and', 2), ('as', 1), ('assume', 2), ('atom', 1), ('belonging', 1), ('belongs', 1), ('celebrate', 1), ('every', 1), ('for', 1), ('good', 1), ('i', 2), ('me', 1), ('myself', 2), ('shall', 1), ('sing', 1), ('to', 2), ('what', 1), ('you', 2)]
        output = self.whitman_splat.types()
        unexpected = self.frankenstein_splat.types()
        self.assertEqual(output, expected)
        self.assertNotEqual(output, unexpected)

    def test_rawtypes(self):
        expected = [('And', 1), ('For', 1), ('I', 2), ('and', 1), ('as', 1), ('assume', 1), ('assume,', 1), ('atom', 1), ('belonging', 1), ('belongs', 1), ('celebrate', 1), ('every', 1), ('good', 1), ('me', 1), ('myself,', 2), ('shall', 1), ('sing', 1), ('to', 2), ('what', 1), ('you', 1), ('you.', 1)]
        output = self.whitman_splat.rawtypes()
        unexpected = self.whitman_splat.types()
        self.assertEqual(output, expected)
        self.assertNotEqual(output, unexpected)

    def test_type_token_ratio(self):
        expected = 0.8163
        output = self.frankenstein_splat.type_token_ratio()
        unexpected = self.whitman_splat.type_token_ratio()
        self.assertEqual(output, expected)
        self.assertNotEqual(output, unexpected)

    def test_syllables(self):
        expected = 25
        output = self.flesch_splat.syllables()
        self.assertLessEqual(abs(expected - output), 1)

    def test_wordcount(self):
        expected = 49
        output = self.frankenstein_splat.wordcount()
        unexpected = self.whitman_splat.wordcount()
        self.assertEqual(output, expected)
        self.assertNotEqual(output, unexpected)

    def test_unique_wordcount(self):
        expected = 18
        output = self.whitman_splat.unique_wordcount()
        unexpected = self.frankenstein_splat.unique_wordcount()
        self.assertEqual(output, expected)
        self.assertNotEqual(output, unexpected)

    def test_content_words(self):
        expected = ['rejoice', 'hear', 'disaster', 'accompanied', 'commencement', 'enterprise', 'regarded', 'evil', 'forebodings', 'arrived', 'yesterday', 'first', 'task', 'assure', 'dear', 'sister', 'welfare', 'increasing', 'confidence', 'success', 'undertaking']
        output = self.frankenstein_splat.content_words()
        unexpected = self.whitman_splat.content_words()
        self.assertEqual(output, expected)
        self.assertNotEqual(output, unexpected)

    def test_function_words(self):
        expected = ['you', 'will', 'to', 'that', 'no', 'has', 'the', 'of', 'an', 'which', 'you', 'have', 'with', 'such', 'i', 'here', 'and', 'my', 'is', 'to', 'my', 'of', 'my', 'and', 'in', 'the', 'of', 'my']
        output = self.frankenstein_splat.function_words()
        unexpected = self.whitman_splat.function_words()
        self.assertEqual(output, expected)
        self.assertNotEqual(output, unexpected)

    def test_content_function_ratio(self):
        expected = 0.75
        output = self.frankenstein_splat.content_function_ratio()
        unexpected = self.whitman_splat.content_function_ratio()
        self.assertEqual(output, expected)
        self.assertNotEqual(output, unexpected)

    def test_unique_content_words(self):
        expected = ['assume', 'atom', 'belonging', 'belongs', 'celebrate', 'every', 'good', 'shall', 'sing']
        output = self.whitman_splat.unique_content_words()
        unexpected = self.frankenstein_splat.unique_content_words()
        self.assertEqual(output, expected)
        self.assertNotEqual(output, unexpected)

    def test_unique_function_words(self):
        expected = ['and', 'as', 'for', 'i', 'me', 'myself', 'to', 'what', 'you']
        output = self.whitman_splat.unique_function_words()
        unexpected = self.frankenstein_splat.unique_function_words()
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
    whitman_splat = SPLAT("tests/whitman_test.txt")
    frankenstein_splat = SPLAT("tests/frankenstein_test.txt")
    flesch_splat = SPLAT("tests/flesch_kincaid_test.txt")
    roark_splat = SPLAT("tests/roark_sample.txt")

    def test_idea_density(self):
        expected = 0.5833
        output = self.whitman_splat.idea_density()
        unexpected = self.frankenstein_splat.idea_density()
        self.assertAlmostEqual(output, expected, 3)
        self.assertNotEqual(output, unexpected)

    def test_content_density(self):
        expected_whitman = 0.846
        output_whitman = self.whitman_splat.content_density()
        self.assertAlmostEqual(output_whitman, expected_whitman, 3)
        expected_frankenstein = 1.130
        output_frankenstein = self.frankenstein_splat.content_density()
        self.assertAlmostEqual(output_frankenstein, expected_frankenstein, 3)
        expected_roark = 1.000
        output_roark = self.roark_splat.content_density()
        self.assertAlmostEqual(output_roark, expected_roark, 3)
        expected_flesch = 1.600
        output_flesch = self.flesch_splat.content_density()
        self.assertAlmostEqual(output_flesch, expected_flesch, 3)

    def test_tree_based_yngve(self):
        expected = 1.1250
        output = self.roark_splat.tree_based_yngve_score()
        unexpected = self.whitman_splat.tree_based_yngve_score()
        self.assertEqual(output, expected)
        self.assertNotEqual(output, unexpected)

    def test_tree_based_frazier(self):
        expected = 0.9375
        output = self.roark_splat.tree_based_frazier_score()
        unexpected = self.whitman_splat.tree_based_frazier_score()
        self.assertEqual(output, expected)
        self.assertNotEqual(output, unexpected)

    def test_flesch_readability(self):
        expected = 37.5
        output = self.flesch_splat.flesch_readability()
        self.assertAlmostEqual(output, expected, 1)

    def test_flesch_kincaid(self):
        expected = 11.3
        output = self.flesch_splat.kincaid_grade_level()
        unexpected = self.whitman_splat.kincaid_grade_level()
        self.assertEqual(output, expected)
        self.assertNotEqual(output, unexpected)

class TestSyllables(unittest.TestCase):

    def test_suffixes(self):
        expected_added = 2
        output_added = SPLAT("added").syllables()
        self.assertEqual(output_added, expected_added)
        expected_apples = 2
        output_apples = SPLAT("apples").syllables()
        self.assertEqual(output_apples, expected_apples)
        expected_foxes = 2
        output_foxes = SPLAT("foxes").syllables()
        self.assertEqual(output_foxes, expected_foxes)
        expected_auntie = 2
        output_auntie = SPLAT("auntie").syllables()
        self.assertEqual(output_auntie, expected_auntie)

    def test_syllabic_l(self):
        expected_mantle = 2
        output_mantle = SPLAT("mantle").syllables()
        self.assertEqual(output_mantle, expected_mantle)
        expected_bottle = 2
        output_bottle = SPLAT("bottle").syllables()
        self.assertEqual(output_bottle, expected_bottle)
        expected_saddle = 2
        output_saddle = SPLAT("saddle").syllables()
        self.assertEqual(output_saddle, expected_saddle)
        expected_poodle = 2
        output_poodle = SPLAT("poodle").syllables()
        self.assertEqual(output_poodle, expected_poodle)
        expected_pistol = 2
        output_pistol = SPLAT("pistol").syllables()
        self.assertEqual(output_pistol, expected_pistol)
        expected_tunnel = 2
        output_tunnel = SPLAT("tunnel").syllables()
        self.assertEqual(output_tunnel, expected_tunnel)

    def test_syllabic_m(self):
        expected_heroism = 4
        output_heroism = SPLAT("heroism").syllables()
        self.assertEqual(output_heroism, expected_heroism)
        expected_feudalism = 4
        output_feudalism = SPLAT("feudalism").syllables()
        self.assertEqual(output_feudalism, expected_feudalism)
        expected_blossom = 2
        output_blossom = SPLAT("blossom").syllables()
        self.assertEqual(output_blossom, expected_blossom)
        expected_rhythm = 2
        output_rhythm = SPLAT("rhythm").syllables()
        self.assertEqual(output_rhythm, expected_rhythm)

    def test_syllabic_n(self):
        expected_cotton = 2
        output_cotton = SPLAT("cotton").syllables()
        self.assertEqual(output_cotton, expected_cotton)
        expected_button = 2
        output_button = SPLAT("button").syllables()
        self.assertEqual(output_button, expected_button)
        expected_risen = 2
        output_risen = SPLAT("risen").syllables()
        self.assertEqual(output_risen, expected_risen)
        expected_prison = 2
        output_prison = SPLAT("prison").syllables()
        self.assertEqual(output_prison, expected_prison)
        expected_sadden = 2
        output_sadden = SPLAT("sadden").syllables()
        self.assertEqual(output_sadden, expected_sadden)
        expected_listen = 2
        output_listen = SPLAT("listen").syllables()
        self.assertEqual(output_listen, expected_listen)
        expected_even = 2
        output_even = SPLAT("even").syllables()
        self.assertEqual(output_even, expected_even)

    def test_syllabic_ng(self):
        expected_going = 2
        output_going = SPLAT("going").syllables()
        self.assertEqual(output_going, expected_going)
        expected_listening = 3
        output_listening = SPLAT("listening").syllables()
        self.assertEqual(output_listening, expected_listening)
        expected_ringing = 2
        output_ringing = SPLAT("ringing").syllables()
        self.assertEqual(output_ringing, expected_ringing)

    def test_syllabic_r(self):
        expected_history = 3
        output_history = SPLAT("history").syllables()
        self.assertEqual(output_history, expected_history)
        expected_hungary = 3
        output_hungary = SPLAT("hungary").syllables()
        self.assertEqual(output_hungary, expected_hungary)
        expected_preference = 3
        output_preference = SPLAT("preference").syllables()
        self.assertEqual(output_preference, expected_preference)

    def test_special_cases(self):
        expected_australian = 3
        output_australian = SPLAT("australian").syllables()
        self.assertEqual(output_australian, expected_australian)
        expected_literal = 3
        output_literal = SPLAT("literal").syllables()
        self.assertEqual(output_literal, expected_literal)
        expected_forebodings = 3
        output_forebodings = SPLAT("forebodings").syllables()
        self.assertEqual(output_forebodings, expected_forebodings)
        expected_pterodactyl = 4
        output_pterodactyl = SPLAT("pterodactyl").syllables()
        #self.assertEqual(output_pterodactyl, expected_pterodactyl)
        self.assertLessEqual(abs(expected_pterodactyl - output_pterodactyl), 1)

    def test_proper_names(self):
        expected_benjamin = 3
        output_benjamin = SPLAT("benjamin").syllables()
        self.assertEqual(output_benjamin, expected_benjamin)
        expected_emily = 3
        output_emily = SPLAT("emily").syllables()
        self.assertEqual(output_emily, expected_emily)
        expected_cissi = 2
        output_cissi = SPLAT("cissi").syllables()
        self.assertEqual(output_cissi, expected_cissi)
        expected_cecilia = 3
        output_cecilia = SPLAT("cecilia").syllables()
        self.assertEqual(output_cecilia, expected_cecilia)
        expected_ares = 2
        output_ares = SPLAT("ares").syllables()
        #self.assertEqual(output_ares, expected_ares)
        self.assertLessEqual(abs(expected_ares - output_ares), 1)

if __name__ == '__main__':
    args = sys.argv
    print(args)
    if len(args) >= 2:
        for arg in args[1:]:
            if arg == "TestSyllables":
                unittest.main()
            elif arg == "TestComplexity":
                pass
            elif arg == "TestParsing":
                pass
            elif arg == "TestBasics":
                pass
            else:
                print("WARNING: Invalid argument " + arg)
                print("Running all tests...")
                unittest.main()
    else:
        unittest.main()
