import unittest

from model.RawNGramminator import RawNGramminator
from model.PunctNGramminator import PunctNGramminator
from model.CaseNGramminator import CaseNGramminator
from model.FullNGramminator import FullNGramminator
from base.TextBubble import TextBubble
from tag.POSTagger import POSTagger
from tokenize.PunctTokenizer import PunctTokenizer
from base.Util import *

class TestBasics(unittest.TestCase):
	whitman = "I celebrate myself, And what I assume you shall assume, For every atom belonging to me as good belongs to you."
	frankenstein = "You will rejoice to hear that no disaster has accompanied the commencement of an enterprise which you have regarded with such evil forebodings."
	raw_ngram = RawNGramminator()
	punct_ngram = PunctNGramminator()
	case_ngram = CaseNGramminator()
	full_ngram = FullNGramminator()
	test_bubble_1 = TextBubble(whitman)
	test_bubble_2 = TextBubble(frankenstein, full_ngram)
	pos_tagger = POSTagger()
	p_tokenizer = PunctTokenizer()

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

	def test_POSTagger_tag(self):
		output = self.pos_tagger.tag(self.whitman.lower())
		expected = [('i', u'PRP'), ('celebrate', u'VB'), ('myself', u'PRP'), (',', u','), ('and', u'CC'), ('what', u'WP'), ('i', u'PRP'), ('assume', u'VB'), ('you', u'PRP'), ('shall', u'MD'), ('assume', u'VB'), (',', u','), ('for', u'IN'), ('every', u'DT'), ('atom', u'NN'), ('belonging', u'VBG'), ('to', u'TO'), ('me', u'PRP'), ('as', u'IN'), ('good', u'JJ'), ('belongs', u'NNS'), ('to', u'TO'), ('you', u'PRP'), ('.', u'.')]
		self.assertEqual(output, expected)
		output = self.pos_tagger.tag(self.whitman.split(" "))
		expected = [('i', u'PRP'), ('celebrate', u'VB'), ('myself', u'PRP'), (',', u','), ('and', u'CC'), ('what', u'WP'), ('i', u'PRP'), ('assume', u'VB'), ('you', u'PRP'), ('shall', u'MD'), ('assume', u'VB'), (',', u','), ('for', u'IN'), ('every', u'DT'), ('atom', u'NN'), ('belonging', u'VBG'), ('to', u'TO'), ('me', u'PRP'), ('as', u'IN'), ('good', u'JJ'), ('belongs', u'NNS'), ('to', u'TO'), ('you', u'PRP'), ('.', u'.')]

		self.assertEqual(output, expected)

	def test_PunctTokenizer(self):
		output = self.p_tokenizer.tokenize(self.whitman)
		expected = ['i', 'celebrate', 'myself', ',', 'and', 'what', 'i', 'assume', 'you', 'shall', 'assume', ',', 'for', 'every', 'atom', 'belonging', 'to', 'me', 'as', 'good', 'belongs', 'to', 'you', '.']
		self.assertEqual(output, expected)

	# def test_Util_tokenize(self):
	# 	# Test String
	# 	text = self.whitman
	# 	output = tokenize(text)
	# 	raw_tokens = output[0]
	# 	clean_tokens = output[1]
	# 	expected_raw = ['I', 'celebrate', 'myself,', 'And', 'what', 'I', 'assume', 'you', 'shall', 'assume,', 'For', 'every', 'atom', 'belonging', 'to', 'me', 'as', 'good', 'belongs', 'to', 'you.']
	# 	expected_clean = ['i', 'celebrate', 'myself', 'and', 'what', 'i', 'assume', 'you', 'shall', 'assume', 'for', 'every', 'atom', 'belonging', 'to', 'me', 'as', 'good', 'belongs', 'to', 'you']
	# 	self.assertEqual(raw_tokens, expected_raw)
	# 	self.assertEqual(clean_tokens, expected_clean)
	#
	# 	# Test List
	# 	text = [self.whitman, self.whitman, self.whitman]
	# 	output = tokenize(text)[0]
	# 	expected = ['I', 'celebrate', 'myself,', 'And', 'what', 'I', 'assume', 'you', 'shall', 'assume,', 'For', 'every', 'atom', 'belonging', 'to', 'me', 'as', 'good', 'belongs', 'to', 'you.', 'I', 'celebrate', 'myself,', 'And', 'what', 'I', 'assume', 'you', 'shall', 'assume,', 'For', 'every', 'atom', 'belonging', 'to', 'me', 'as', 'good', 'belongs', 'to', 'you.', 'I', 'celebrate', 'myself,', 'And', 'what', 'I', 'assume', 'you', 'shall', 'assume,', 'For', 'every', 'atom', 'belonging', 'to', 'me', 'as', 'good', 'belongs', 'to', 'you.']
	# 	self.assertEqual(output, expected)
	#
	# 	# Test File
	# 	text_file = "test_data/whitman_test.txt"
	# 	output = tokenize(text_file)[0]
	# 	expected = ['I', 'celebrate', 'myself,', 'And', 'what', 'I', 'assume', 'you', 'shall', 'assume,', 'For', 'every', 'atom', 'belonging', 'to', 'me', 'as', 'good', 'belongs', 'to', 'you.']
	# 	self.assertEqual(output, expected)

	# def test_Util_sentenize(self):
	# 	# Test String
	# 	text = (self.whitman + " ")*3
	# 	output = sentenize(text)
	# 	expected = ['I celebrate myself, And what I assume you shall assume, For every atom belonging to me as good belongs to you.', 'I celebrate myself, And what I assume you shall assume, For every atom belonging to me as good belongs to you.', 'I celebrate myself, And what I assume you shall assume, For every atom belonging to me as good belongs to you.']
	# 	self.assertEqual(output, expected)
	#
	# 	# Test List
	# 	text = [self.whitman, self.whitman, self.whitman]
	# 	output = sentenize(text)
	# 	expected = ['I celebrate myself, And what I assume you shall assume, For every atom belonging to me as good belongs to you.', 'I celebrate myself, And what I assume you shall assume, For every atom belonging to me as good belongs to you.', 'I celebrate myself, And what I assume you shall assume, For every atom belonging to me as good belongs to you.']
	# 	self.assertEqual(output, expected)
	#
	# 	# Test File
	# 	text_file = "test_data/lorem_sample.txt"
	# 	output = sentenize(text_file)
	# 	expected = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 'Maecenas semper nisl fermentum auctor facilisis.', 'Pellentes que vehicula pharetra leo, ornare vehicula neque cursus id.', 'Maecenas commodo sapien sed purus mollis condimentum.', 'Nulla ultricies sapien nec urna consectetur, non vulputate elit faucibus.', 'Nulla in luctus arcu.', 'Nunc sit amet accumsan purus.', 'Donec lectus nulla, aliquet et dui in, ullamcorper tincidunt nibh.', 'Duis iaculis mi risus.', 'Phasellus id volutpat ex, a imperdiet diam.', 'Maecenas eu tellus a dui ultricies placerat.', 'Pellentesque magna nibh, vulputate et elit eget, tristique facilisis tellus.', 'Aliquam quis neque tortor.', 'Phasellus vitae elit ut ante consequat varius.']
	# 	self.assertEqual(output, expected)


if __name__ == '__main__':
	unittest.main()
