import unittest
from nltk.corpus import brown
from model.RawNGramminator import RawNGramminator
from model.PunctNGramminator import PunctNGramminator
from model.CaseNGramminator import CaseNGramminator
from model.FullNGramminator import FullNGramminator
from base.TextBubble import TextBubble

class TestBasics(unittest.TestCase):
	whitman = "I celebrate myself, And what I assume you shall assume, For every atom belonging to me as good belongs to you."
	frankenstein = "You will rejoice to hear that no disaster has accompanied the commencement of an enterprise which you have regarded with such evil forebodings."
	raw_ngram = RawNGramminator()
	punct_ngram = PunctNGramminator()
	case_ngram = CaseNGramminator()
	full_ngram = FullNGramminator()
	test_bubble_1 = TextBubble(whitman)
	test_bubble_2 = TextBubble(frankenstein, full_ngram)

	def test_RawNGramminator(self):
		output = self.raw_ngram.ngrams(self.whitman, 2)
		expected = [('I', 'celebrate'), ('celebrate', 'myself,'), ('myself,', 'And'), ('And', 'what'), ('what', 'I'), ('I', 'assume'), ('assume', 'you'), ('you', 'shall'), ('shall', 'assume,'), ('assume,', 'For'), ('For', 'every'), ('every', 'atom'), ('atom', 'belonging'), ('belonging', 'to'), ('to', 'me'), ('me', 'as'), ('as', 'good'), ('good', 'belongs'), ('belongs', 'to'), ('to', 'you.')]
		self.assertEqual(output, expected)
		self.assertNotEqual(output, self.raw_ngram.ngrams(self.frankenstein, 2))

	def test_PunctNGramminator(self):
		output = self.punct_ngram.ngrams(self.whitman, 2)
		expected = [('I', 'celebrate'), ('celebrate', 'myself'), ('myself', 'And'), ('And', 'what'), ('what', 'I'), ('I', 'assume'), ('assume', 'you'), ('you', 'shall'), ('shall', 'assume'), ('assume', 'For'), ('For', 'every'), ('every', 'atom'), ('atom', 'belonging'), ('belonging', 'to'), ('to', 'me'), ('me', 'as'), ('as', 'good'), ('good', 'belongs'), ('belongs', 'to'), ('to', 'you')]
		self.assertEqual(output, expected)
		self.assertNotEqual(output, self.punct_ngram.ngrams(self.frankenstein, 2))

	def test_CaseNGramminator(self):
		output = self.case_ngram.ngrams(self.whitman, 2)
		expected = [('i', 'celebrate'), ('celebrate', 'myself,'), ('myself,', 'and'), ('and', 'what'), ('what', 'i'), ('i', 'assume'), ('assume', 'you'), ('you', 'shall'), ('shall', 'assume,'), ('assume,', 'for'), ('for', 'every'), ('every', 'atom'), ('atom', 'belonging'), ('belonging', 'to'), ('to', 'me'), ('me', 'as'), ('as', 'good'), ('good', 'belongs'), ('belongs', 'to'), ('to', 'you.')]
		self.assertEqual(output, expected)
		self.assertNotEqual(output, self.case_ngram.ngrams(self.frankenstein, 2))

	def test_FullNGramminator(self):
		output = self.full_ngram.ngrams(self.whitman, 2)
		expected = [('i', 'celebrate'), ('celebrate', 'myself'), ('myself', 'and'), ('and', 'what'), ('what', 'i'), ('i', 'assume'), ('assume', 'you'), ('you', 'shall'), ('shall', 'assume'), ('assume', 'for'), ('for', 'every'), ('every', 'atom'), ('atom', 'belonging'), ('belonging', 'to'), ('to', 'me'), ('me', 'as'), ('as', 'good'), ('good', 'belongs'), ('belongs', 'to'), ('to', 'you')]
		self.assertEqual(output, expected)
		self.assertNotEqual(output, self.full_ngram.ngrams(self.frankenstein, 2))

	def test_TextBubble_rawtokens(self):
		output = self.test_bubble_1.rawtokens()
		expected = ['I', 'celebrate', 'myself,', 'And', 'what', 'I', 'assume', 'you', 'shall', 'assume,', 'For', 'every', 'atom', 'belonging', 'to', 'me', 'as', 'good', 'belongs', 'to', 'you.']
		self.assertEqual(output, expected)
		self.assertNotEqual(output, self.test_bubble_2.rawtokens())

	def test_TextBubble_tokens(self):
		output = self.test_bubble_1.tokens()
		expected = ['i', 'celebrate', 'myself', 'and', 'what', 'i', 'assume', 'you', 'shall', 'assume', 'for', 'every', 'atom', 'belonging', 'to', 'me', 'as', 'good', 'belongs', 'to', 'you']
		self.assertEqual(output, expected)
		self.assertNotEqual(output, self.test_bubble_2.tokens())

	def test_TextBubble_rawtypes(self):
		output = self.test_bubble_1.rawtypes()
		expected = [('And', 1), ('For', 1), ('I', 2), ('as', 1), ('assume', 1), ('assume,', 1), ('atom', 1), ('belonging', 1), ('belongs', 1), ('celebrate', 1), ('every', 1), ('good', 1), ('me', 1), ('myself,', 1), ('shall', 1), ('to', 2), ('what', 1), ('you', 1), ('you.', 1)]
		self.assertEqual(output, expected)
		self.assertNotEqual(output, self.test_bubble_2.rawtypes())

	def test_TextBubble_types(self):
		output = self.test_bubble_1.types()
		expected = [('and', 1), ('as', 1), ('assume', 2), ('atom', 1), ('belonging', 1), ('belongs', 1), ('celebrate', 1), ('every', 1), ('for', 1), ('good', 1), ('i', 2), ('me', 1), ('myself', 1), ('shall', 1), ('to', 2), ('what', 1), ('you', 2)]
		self.assertEqual(output, expected)
		self.assertNotEqual(output, self.test_bubble_2.types())

	def test_TextBubble_bubble(self):
		output = self.test_bubble_1.bubble()
		expected = self.whitman
		self.assertEqual(output, expected)
		self.assertNotEqual(output, self.test_bubble_2.bubble())

	def test_TextBubble_sents(self):
		output = self.test_bubble_1.sents()
		expected = [self.whitman]
		self.assertEqual(output, expected)
		self.assertNotEqual(output, self.test_bubble_2.sents())

	def test_TextBubble_sentcount(self):
		output = self.test_bubble_1.sentcount()
		expected = 1
		unexpected = 4
		self.assertEqual(output, expected)
		self.assertNotEqual(output, unexpected)

	def test_TextBubble_wordcount(self):
		output = self.test_bubble_1.wordcount()
		expected = 21
		self.assertEqual(output, expected)
		self.assertNotEqual(output, self.test_bubble_2.wordcount())

	def test_TextBubble_unique_wordcount(self):
		output = self.test_bubble_1.unique_wordcount()
		expected = 17
		self.assertEqual(output, expected)
		self.assertNotEqual(output, self.test_bubble_2.unique_wordcount())

	def test_TextBubble_type_token_ratio(self):
		output = self.test_bubble_1.type_token_ratio()
		expected = 80.9524
		self.assertEqual(output, expected)
		self.assertNotEqual(output, self.test_bubble_2.type_token_ratio())

	def test_TextBubble_ngrams(self):
		output = self.test_bubble_2.ngrams(2)
		expected = [('you', 'will'), ('will', 'rejoice'), ('rejoice', 'to'), ('to', 'hear'), ('hear', 'that'), ('that', 'no'), ('no', 'disaster'), ('disaster', 'has'), ('has', 'accompanied'), ('accompanied', 'the'), ('the', 'commencement'), ('commencement', 'of'), ('of', 'an'), ('an', 'enterprise'), ('enterprise', 'which'), ('which', 'you'), ('you', 'have'), ('have', 'regarded'), ('regarded', 'with'), ('with', 'such'), ('such', 'evil'), ('evil', 'forebodings')]
		unexpected = [('i', 'celebrate'), ('celebrate', 'myself'), ('myself', 'and'), ('and', 'what'), ('what', 'i'), ('i', 'assume'), ('assume', 'you'), ('you', 'shall'), ('shall', 'assume'), ('assume', 'for'), ('for', 'every'), ('every', 'atom'), ('atom', 'belonging'), ('belonging', 'to'), ('to', 'me'), ('me', 'as'), ('as', 'good'), ('good', 'belongs'), ('belongs', 'to'), ('to', 'you')]
		self.assertEqual(output, expected)
		self.assertNotEqual(output, unexpected)

	def test_TextBubble_unigrams(self):
		output = self.test_bubble_2.unigrams()
		expected = [('you',), ('will',), ('rejoice',), ('to',), ('hear',), ('that',), ('no',), ('disaster',), ('has',), ('accompanied',), ('the',), ('commencement',), ('of',), ('an',), ('enterprise',), ('which',), ('you',), ('have',), ('regarded',), ('with',), ('such',), ('evil',), ('forebodings',)]
		unexpected = self.test_bubble_1.unigrams()
		self.assertEqual(output, expected)
		self.assertNotEqual(output, unexpected)

	def test_TextBubble_bigrams(self):
		output = self.test_bubble_2.bigrams()
		expected = [('you', 'will'), ('will', 'rejoice'), ('rejoice', 'to'), ('to', 'hear'), ('hear', 'that'), ('that', 'no'), ('no', 'disaster'), ('disaster', 'has'), ('has', 'accompanied'), ('accompanied', 'the'), ('the', 'commencement'), ('commencement', 'of'), ('of', 'an'), ('an', 'enterprise'), ('enterprise', 'which'), ('which', 'you'), ('you', 'have'), ('have', 'regarded'), ('regarded', 'with'), ('with', 'such'), ('such', 'evil'), ('evil', 'forebodings')]
		unexpected = self.test_bubble_1.bigrams()
		self.assertEqual(output, expected)
		self.assertNotEqual(output, unexpected)

	def test_TextBubble_trigrams(self):
		output = self.test_bubble_2.trigrams()
		expected = [('you', 'will', 'rejoice'), ('will', 'rejoice', 'to'), ('rejoice', 'to', 'hear'), ('to', 'hear', 'that'), ('hear', 'that', 'no'), ('that', 'no', 'disaster'), ('no', 'disaster', 'has'), ('disaster', 'has', 'accompanied'), ('has', 'accompanied', 'the'), ('accompanied', 'the', 'commencement'), ('the', 'commencement', 'of'), ('commencement', 'of', 'an'), ('of', 'an', 'enterprise'), ('an', 'enterprise', 'which'), ('enterprise', 'which', 'you'), ('which', 'you', 'have'), ('you', 'have', 'regarded'), ('have', 'regarded', 'with'), ('regarded', 'with', 'such'), ('with', 'such', 'evil'), ('such', 'evil', 'forebodings')]
		unexpected = self.test_bubble_1.trigrams()
		self.assertEqual(output, expected)
		self.assertNotEqual(output, unexpected)

	def test_TextBubble_splat(self):
		output = self.test_bubble_1.splat()
		expected = "===== Bubble:\n"
		expected += "I celebrate myself, And what I assume you shall assume, For every atom belonging to me as good belongs to you.\n"
		expected += "===== Sentences:\n"
		expected += "[0] I celebrate myself, And what I assume you shall assume, For every atom belonging to me as good belongs to you.\n"
		expected += "Sentence Count: 1\n"
		expected += "===== Tokens:\n"
		expected += "['i', 'celebrate', 'myself', 'and', 'what', 'i', 'assume', 'you', 'shall', 'assume', 'for', 'every', 'atom', 'belonging', 'to', 'me', 'as', 'good', 'belongs', 'to', 'you']\n"
		expected += "Word Count: 21\n"
		expected += "===== Types:\n"
		expected += "[('and', 1), ('as', 1), ('assume', 2), ('atom', 1), ('belonging', 1), ('belongs', 1), ('celebrate', 1), ('every', 1), ('for', 1), ('good', 1), ('i', 2), ('me', 1), ('myself', 1), ('shall', 1), ('to', 2), ('what', 1), ('you', 2)]\n"
		expected += "Unique Word Count: 17\n"
		expected += "===== Type-Token Ratio:\n"
		expected += "80.9524\n"
		self.assertEqual(output, expected)

if __name__ == '__main__':
	unittest.main()
