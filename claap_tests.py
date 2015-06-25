import unittest
from claap_functions import *

class TestBasics(unittest.TestCase):
	
	def test_tokens(self):
		testing = get_tokens('whitman_test.txt')
		expecting = ['I', 'celebrate', 'myself,', 'And', 'what', 'I', 'assume', 'you', 'shall', 'assume,', 'For', 'every', 'atom', 'belonging', 'to', 'me', 'as', 'good', 'belongs', 'to', 'you.']
		self.assertEqual(testing, expecting)

	def test_types(self):
		testing = get_types('whitman_test.txt')
		expecting = set(['And', 'assume,', 'what', 'good', 'to', 'For', 'myself,', 'I', 'shall', 'belonging', 'me', 'assume', 'as', 'belongs', 'every', 'you.', 'atom', 'you', 'celebrate'])
		self.assertEqual(testing, expecting)

	def test_ttr1(self):
		testing = get_TTR('whitman_test.txt')
		expecting = 90.48
		self.assertEqual(testing, expecting)

	def test_ttr2(self):
		testing = get_TTR('lorem_ipsum.txt')
		expecting = 48.9
		self.assertEqual(testing, expecting)

	def test_word_count1(self):
		testing = get_word_count('whitman_test.txt')
		expecting = 21
		self.assertEqual(testing, expecting)

	def test_word_count2(self):
		testing = get_word_count('lorem_ipsum.txt')
		expecting = 454
		self.assertEqual(testing, expecting)

	def test_word_count3(self):
		testing = get_word_count('gutenberg_data/moby_dick.txt')
		expecting = 215304
		self.assertEqual(testing, expecting)

	def test_unique_word_count(self):
		testing = get_unique_word_count('gutenberg_data/moby_dick.txt')
		expecting = 33226
		self.assertEqual(testing, expecting)

if __name__ == '__main__':
    unittest.main()
