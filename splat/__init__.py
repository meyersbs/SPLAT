#!/usr/bin/env python

""" Defines objects/constants for the splat module. """

__author__ = "Benjamin S. Meyers"
__copyright__ = "Copyright 2015-2017, Benjamin S. Meyers"
__credits__ = ["Benjamin S. Meyers"]
__version__ = "1.0.0"
__maintainer__ = "Benjamin S. Meyers"
__email__ = "ben@splat-library.org"
__status__ = "Development"

#### IMPORTS ###################################################################
from nltk.corpus import wordnet

from splat.config import Configuration
from splat.logger import Logger
from splat.sentence import Sentence
from splat.word import Word

CONFIG = Configuration()
LOGGER = Logger()
UNCERTAINTY_MAP = {'E': 'Epistemic', 'D': 'Doxastic', 'I': 'Investiation',
                   'N': 'Condition', 'U': 'Uncertain', 'C': 'Certain'}
WORDNET_POS_MAP = {'N': wordnet.NOUN, 'V': wordnet.VERB, 'J': wordnet.ADJ,
                   'R': wordnet.ADV}
SUPPORTED_LANGS = ['danish', 'dutch', 'english', 'finnish', 'french', 'german',
                   'hungarian', 'italian', 'kazakh', 'norwegian', 'portuguese',
                   'russian', 'spanish', 'swedish', 'turkish']
FIXES_EN = {"'m": 'am', "'ll": 'will', "n't": 'not', "'ve": 'have',
            "'re": 'are', "won't": 'will not', "can't": 'can not',
            "aren't": 'are not', "wouldn't": 'would not',
            "couldn't": 'could not', "shouldn't": 'should not',
            "would've": 'would have', "could've": 'could have',
            "should've": 'should have', "i'll": 'i will', "she'll": 'she will',
            "he'll": 'he will', "they'll": 'they will', "you'll": 'you will',
            "we'll": 'we will', "they're": 'they are', "you're": 'you are',
            "we're": 'we are', "they've": 'they have', "we've": 'we have',
            "you've": 'you have', "i've": 'i have'}




