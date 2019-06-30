#!/usr/bin/env python3

"""

Defines a wrapper object for words.

By design, aspects of a ``Word`` can only be accessed as properties. The
functions for getting and setting these properties are hidden.

"""

__author__ = "Benjamin S. Meyers"
__copyright__ = "Copyright (c) 2015-2019, Benjamin S. Meyers"
__credits__ = []
__version__ = ""
__maintainer = "Benjamin S. Meyers"
__email__ = "ben@splat.dev"
__status__ = "development"

#### IMPORTS ###################################################################
from splat import LOGGER

#### CLASSES ###################################################################
class Word(object):
    def __init__(self, word, pos, stem, chunk, lemma, syllables):
        """
        Instantiate a Word object with the given parameters.

        :param word: plaintext word
        :type word: str
        :param pos: part-of-speech tag for the word
        :type pos: str
        :param stem: stem of the word
        :type stem: str
        :param chunk: chunk tag of the word
        :type chunk: str
        :param lemma: lemma of the word
        :type lemma: str
        :param syllables: number of syllables in the word
        :type syllables: int
        """
        self._word = word
        self._pos = pos
        self._stem = stem
        self._chunk = chunk
        self._lemma = lemma
        self._syllables = syllables
        self._uncertainty = None

    def __str__(self):
        """
        Get the str representation of this Word object.

        :return: str
        """
        return str(self.__dict__())

    def __dict__(self):
        """
        Get the dict representation of this Word object.

        :return: dict
        """
        d = {'word': self._word, 'pos': self._pos, 'stem': self._stem,
             'chunk': self._chunk, 'lemma': self._lemma,
             'syllables': self._syllables, 'uncertainty': self._uncertainty}
        return d

    #### FUNCTIONS #############################################################
    def __get_word(self):
        """
        Get the current value of self._word.

        :return: str
        """
        LOGGER.get("'word': '{0}'".format(self._word))
        return self._word

    def __get_pos(self):
        """
        Get the current value of self._pos.

        :return: str
        """
        LOGGER.get("'pos': '{0}'".format(self._pos))
        return self._pos

    def __set_pos(self, pos):
        """
        Update the value of self._pos.

        :param pos:
        :type pos: str
        :return: None
        """
        self._pos = pos
        LOGGER.set("'pos': '{0}'".format(self._pos))

    def __get_stem(self):
        """
        Get the current value of self._stem.

        :return: str
        """
        LOGGER.get("'stem': '{0}'".format(self._stem))
        return self._stem

    def __set_stem(self, stem):
        """
        Update the value of self._stem.

        :param stem:
        :type stem: str
        :return: None
        """
        self._stem = stem
        LOGGER.set("'stem': '{0}'".format(self._stem))

    def __get_chunk(self):
        """
        Get the current value of self._chunk.

        :return: str
        """
        LOGGER.get("'chunk': '{0}'".format(self._chunk))
        return self._chunk

    def __set_chunk(self, chunk):
        """
        Update the value of self._chunk.

        :param chunk:
        :type chunk: str
        :return: None
        """
        self._chunk = chunk
        LOGGER.set("'chunk': '{0}'".format(self._chunk))

    def __get_lemma(self):
        """
        Get the current value of self._lemma.

        :return: str
        """
        LOGGER.get("'lemma': '{0}'".format(self._lemma))
        return self._lemma

    def __set_lemma(self, lemma):
        """
        Update the value of self._lemma.

        :param lemma:
        :type lemma: str
        :return: None
        """
        self._lemma = lemma
        LOGGER.set("'lemma': '{0}'".format(self._lemma))

    def __get_syllables(self):
        """
        Get the current value of self._syllables.

        :return: int
        """
        LOGGER.get("'syllables': '{0}'".format(self._syllables))
        return self._syllables

    def __set_syllables(self, syllables):
        """
        Update the value of self._syllables.

        :param syllables:
        :type syllables: int
        :return: None
        """
        self._syllables = syllables
        LOGGER.set("'syllables': '{0}'".format(self._syllables))

    def __get_uncertainty(self):
        """
        Get the current value of self._uncertainty.

        :return: str or None
        """
        LOGGER.get("'uncertainty': '{0}'".format(self._uncertainty))
        return self._uncertainty

    def __set_uncertainty(self, uncertainty):
        """
        Update the value of self._uncertainty.

        :param uncertainty:
        :type uncertainty: str
        :return: None
        """
        self._uncertainty = uncertainty
        LOGGER.set("'uncertainty': '{0}'".format(self._uncertainty))

    #### PROPERTIES ############################################################
    word = property(fget=__get_word,
                    doc="The plaintext representation of the this Word object.")

    pos = property(fget=__get_pos, fset=__set_pos,
                   doc="Access the part-of-speech tag for this Word object.")

    stem = property(fget=__get_stem, fset=__set_stem,
                    doc="Access the stem for this Word object.")

    chunk = property(fget=__get_chunk, fset=__set_chunk,
                     doc="Access the chunk for this Word object.")

    lemma = property(fget=__get_lemma, fset=__set_lemma,
                     doc="Access the lemma for this Word object.")

    syllables = property(fget=__get_syllables, fset=__set_syllables,
                         doc="Access the number of syllables in this Word"
                             "object.")

    uncertainty = property(fget=__get_uncertainty, fset=__set_uncertainty,
                           doc="Access the uncertainty for this Word object.")


