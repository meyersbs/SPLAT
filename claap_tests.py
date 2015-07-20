import unittest
from claap_functions import *


class TestBasics(unittest.TestCase):
    def test_tokens1(self):
        testing = get_tokens('test_data/whitman_test.txt')
        expecting = ['I', 'celebrate', 'myself,', 'And', 'what', 'I', 'assume', 'you', 'shall', 'assume,', 'For',
                     'every', 'atom', 'belonging', 'to', 'me', 'as', 'good', 'belongs', 'to', 'you.']
        self.assertEqual(testing, expecting)

    def test_tokens2(self):
        arg1 = get_tokens('test_data/whitman_test.txt')
        arg2 = get_tokens('test_data/lorem_ipsum.txt')
        self.assertNotEqual(arg1, arg2)

    def test_types1(self):
        testing = get_types('test_data/whitman_test.txt')
        expecting = set(['And', 'assume,', 'what', 'good', 'to', 'For', 'myself,', 'I', 'shall', 'belonging', 'me', 'assume', 'as',
             'belongs', 'every', 'you.', 'atom', 'you', 'celebrate'])
        self.assertEqual(testing, expecting)

    def test_types2(self):
        arg1 = get_types('test_data/whitman_test.txt')
        arg2 = get_types('test_data/lorem_ipsum.txt')
        self.assertNotEqual(arg1, arg2)

    def test_ttr1(self):
        testing = get_ttr('test_data/whitman_test.txt')
        expecting = 90.48
        self.assertEqual(testing, expecting)

    def test_ttr2(self):
        arg1 = get_ttr('test_data/lorem_ipsum.txt')
        arg2 = 15.0
        self.assertNotEqual(arg1, arg2)

    def test_word_count1(self):
        testing = get_word_count('test_data/whitman_test.txt')
        expecting = 21
        self.assertEqual(testing, expecting)

    def test_word_count2(self):
        arg1 = get_word_count('test_data/lorem_ipsum.txt')
        arg2 = get_word_count('test_data/moby_dick.txt')
        self.assertNotEqual(arg1, arg2)

    def test_unique_word_count1(self):
        testing = get_unique_word_count('test_data/moby_dick.txt')
        expecting = 33226
        self.assertEqual(testing, expecting)

    def test_unique_word_count2(self):
        arg1 = get_unique_word_count('test_data/lorem_ipsum.txt')
        arg2 = get_unique_word_count('test_data/frankenstein.txt')
        self.assertNotEqual(arg1, arg2)


if __name__ == '__main__':
    unittest.main()
