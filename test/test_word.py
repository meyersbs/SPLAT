#!/usr/bin/env python3

""" Defines unittests for splat/word.py """

__author__ = "Benjamin S. Meyers"
__copyright__ = "Copyright (c) 2015-2019, Benjamin S. Meyers"
__credits__ = []
__version__ = ""
__maintainer = "Benjamin S. Meyers"
__email__ = "ben@splat.dev"
__status__ = "development"

#### IMPORTS ###################################################################
import unittest

from splat.word import Word

#### CLASSES ###################################################################
class TestWord(unittest.TestCase):
    def test_dict(self):
        """
        Test function __dict__() from Word class.

        :return: None
        """
        w = Word("apple", "NN", "appl", "B-NP", "apple", 2)
        expected = {'word': 'apple', 'pos': 'NN', 'stem': 'appl',
                    'chunk': 'B-NP', 'lemma': 'apple', 'syllables': 2,
                    'uncertainty': None}
        actual = w.__dict__()
        self.assertDictEqual(expected, actual)

    def test_str(self):
        """
        Test function __str__() from Word class.

        :return: None
        """
        w = Word("apple", "NN", "appl", "B-NP", "apple", 2)
        expected = "{'word': 'apple', 'pos': 'NN', 'stem': 'appl', 'chunk':" \
                   " 'B-NP', 'lemma': 'apple', 'syllables': 2, 'uncertainty':" \
                   " None}"
        actual = w.__str__()
        self.assertEqual(expected, actual)

    def test_word_property_get(self):
        """
        Test property 'word' from Word class.

        :return: None
        """
        w = Word("apple", "NN", "appl", "B-NP", "apple", 2)
        expected = "apple"
        actual = w.word
        self.assertEqual(expected, actual)

    def test_word_property_set(self):
        """
        Test property 'word' from Word class.

        :return: None
        """
        w = Word("apple", "NN", "appl", "B-NP", "apple", 2)
        with self.assertRaises(AttributeError):
            w.word = "blah"

    def test_pos_property_get(self):
        """
        Test property 'pos' from Word class.

        :return: None
        """
        w = Word("apple", "NN", "appl", "B-NP", "apple", 2)
        expected = "NN"
        actual = w.pos
        self.assertEqual(expected, actual)

    def test_pos_property_set(self):
        """
        Test property 'pos' from Word class.

        :return: None
        """
        w = Word("apple", "VBD", "appl", "B-NP", "apple", 2)
        w.pos = "NN"
        expected = "NN"
        actual = w.pos
        self.assertEqual(expected, actual)

    def test_stem_property_get(self):
        """
        Test property 'stem' from Word class.

        :return: None
        """
        w = Word("apple", "NN", "appl", "B-NP", "apple", 2)
        expected = "appl"
        actual = w.stem
        self.assertEqual(expected, actual)

    def test_stem_property_set(self):
        """
        Test property 'stem' from Word class.

        :return: None
        """
        w = Word("apple", "NN", "apple", "B-NP", "apple", 2)
        w.stem = "appl"
        expected = "appl"
        actual = w.stem
        self.assertEqual(expected, actual)

    def test_chunk_property_get(self):
        """
        Test property 'chunk' from Word class.

        :return: None
        """
        w = Word("apple", "NN", "appl", "B-NP", "apple", 2)
        expected = "B-NP"
        actual = w.chunk
        self.assertEqual(expected, actual)

    def test_chunk_property_set(self):
        """
        Test property 'chunk' from Word class.

        :return: None
        """
        w = Word("apple", "NN", "appl", "I-NP", "apple", 2)
        w.chunk = "B-NP"
        expected = "B-NP"
        actual = w.chunk
        self.assertEqual(expected, actual)

    def test_lemma_property_get(self):
        """
        Test property 'lemma' from Word class.

        :return: None
        """
        w = Word("apple", "NN", "appl", "B-NP", "apple", 2)
        expected = "apple"
        actual = w.lemma
        self.assertEqual(expected, actual)

    def test_lemma_property_set(self):
        """
        Test property 'lemma' from Word class.

        :return: None
        """
        w = Word("apple", "NN", "appl", "B-NP", "appl", 2)
        w.lemma = "apple"
        expected = "apple"
        actual = w.lemma
        self.assertEqual(expected, actual)

    def test_syllables_property_get(self):
        """
        Test property 'syllables' from Word class.

        :return: None
        """
        w = Word("apple", "NN", "appl", "B-NP", "apple", 2)
        expected = 2
        actual = w.syllables
        self.assertEqual(expected, actual)

    def test_syllables_property_set(self):
        """
        Test property 'syllables' from Word class.

        :return: None
        """
        w = Word("apple", "NN", "appl", "B-NP", "apple", 1)
        w.syllables = 2
        expected = 2
        actual = w.syllables
        self.assertEqual(expected, actual)

    def test_uncertainty_property_get(self):
        """
        Test property 'uncertainty' from Word class.

        :return: None
        """
        w = Word("apple", "NN", "appl", "B-NP", "apple", 2)
        expected = None
        actual = w.uncertainty
        self.assertEqual(expected, actual)

    def test_uncertainty_property_set(self):
        """
        Test property 'uncertainty' from Word class.

        :return: None
        """
        w = Word("apple", "NN", "appl", "B-NP", "apple", 1)
        w.uncertainty = "C"
        expected = "C"
        actual = w.uncertainty
        self.assertEqual(expected, actual)
