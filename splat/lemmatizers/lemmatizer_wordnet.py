#!/usr/bin/env python

""" Defines a lemmatizer based on NLTK's WordNetLemmatizer. """

__author__ = "Benjamin S. Meyers"
__copyright__ = "Copyright 2015-2017, Benjamin S. Meyers"
__credits__ = ["Benjamin S. Meyers"]
__version__ = "1.0.0"
__maintainer__ = "Benjamin S. Meyers"
__email__ = "ben@splat-library.org"
__status__ = "Development"

#### IMPORTS ###################################################################
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer as wordnet_lemmatizer

from splat import WORDNET_POS_MAP
from splat.lemmatizers import lemmatizer


class WordNetLemmatizer(lemmatizer.Lemmatizer):
    """ Implements splat.lemmatizers.lemmatizer interface. """
    def __init__(self):
        """ Instantiate a WordNetLemmatizer object. """
        super(WordNetLemmatizer, self).__init__()
        self.lemmatizer = wordnet_lemmatizer()

    def lemmatize(self, tokens, pos_tags):
        """
        Determine lemmas for each of the given tokens.

        :param tokens: tokens
        :type tokens: list
        :param pos_tags: part-of-speech tags
        :type pos_tags: list
        :return: list
        """
        lemmas = []

        tokens = [(t, WORDNET_POS_MAP.get(p[0], wordnet.NOUN))
                  for (t, pos) in zip(tokens, pos_tags)]

        for (token, pos) in tokens:
            lemmas.append(self.lemmatizer.lemmatize(token, pos))

        return lemmas
