#!/usr/bin/env python

""" Defines an object to facilitate manipulating stopword lists. """

__author__ = "Benjamin S. Meyers"
__copyright__ = "Copyright 2015-2017, Benjamin S. Meyers"
__credits__ = ["Benjamin S. Meyers"]
__version__ = "1.0.0"
__maintainer__ = "Benjamin S. Meyers"
__email__ = "ben@splat-library.org"
__status__ = "Development"

#### IMPORTS ###################################################################
from nltk.corpus import stopwords
from splat import LOGGER, SUPPORTED_LANGS


class StopWords(object):
    def __init__(self, language):
        """ Instantiate a StopWords object. """
        self._language = language
        if language.lower() in SUPPORTED_LANGS:
            self._stopwords = stopwords.words(language)
        else:
            self._stopwords = [None]
            LOGGER.warn("No stopwords available for '{0}'.".format(language))

    def get(self):
        """
        Get the current value of self._stopwords
        :return: list
        """
        LOGGER.get("'stopwords': {0}".format(self._stopwords))
        return self._stopwords

    def add(self, words):
        """
        Update the value of self._stopwords by adding the given words.

        :param words:
        :type words: list
        :return:
        """
        for word in words:
            if word not in self._stopwords:
                self._stopwords.append(word)

        LOGGER.set("'stopwords': {0}".format(self._stopwords))

    def remove(self, words):
        """
        Update the value of self._stopwords by removing the given words.

        :param words:
        :type words: list
        :return:
        """
        for word in words:
            for _ in range(self._stopwords.count(word)):
                self._stopwords.remove(word)

        LOGGER.set("'stopwords': {0}".format(self._stopwords))

    def set(self, words):
        """
        Overwrite the value of self._stopwords with the given words.

        :param words:
        :type words: list
        :return:
        """
        self._stopwords = words
        LOGGER.set("'stopwords': {0}".format(self._stopwords))
