#!/usr/bin/env python

""" Defines a wrapper objects for words. """

__author__ = "Benjamin S. Meyers"
__copyright__ = "Copyright 2015-2017, Benjamin S. Meyers"
__credits__ = ["Benjamin S. Meyers"]
__version__ = "1.0.0"
__maintainer__ = "Benjamin S. Meyers"
__email__ = "ben@splat-library.org"
__status__ = "Development"

#### IMPORTS ###################################################################
from splat import LOGGER, UNCERTAINTY_MAP

class Word(object):
    def __init__(self, word, pos, stem, chunk, lemma, syllables):
        """
        Instantiate a Word object with the given parameters.

        :param word:
        :type word: str
        :param pos:
        :type pos: str
        :param stem:
        :type stem: str
        :param chunk:
        :type chunk: str
        :param lemma: 
        :type lemma: str
        :param syllables:
        :type syllables: str
        """
        self._word = word
        self._pos = pos
        self._stem = stem
        self._chunk = chunk
        self._lemma = lemma
        self._syllables = syllables
        self._uncertainty = None

    def _get_word(self):
        """
        Get the current value of self._word.

        :return: str
        """
        LOGGER.get("'word': '{0}'".format(self._word))
        return self._word

    def _set_word(self, word):
        """
        Update the value of self._word.

        :param word:
        :type word: str
        :return:
        """
        self._word = word
        LOGGER.set("'word': '{0}'".format(self._word))

    word = property(fget=_get_word, fset=_set_word,
                    doc="The plaintext representation of the this Word object.")

    def _get_pos(self):
        """
        Get the current value of self._pos.

        :return: str
        """
        LOGGER.get("'pos': '{0}'".format(self._pos))
        return self._pos

    def _set_pos(self, pos):
        """
        Update the value of sel._pos.

        :param pos:
        :type pos: str
        :return:
        """
        self._pos = pos
        LOGGER.get("'pos': '{0}'".format(self._pos))

    pos = property(fget=_get_pos, fset=_set_pos,
                   doc="The part-of-speech tag for this Word object.")

    def _get_stem(self):
        """
        Get the current value of self._stem.

        :return: str
        """
        LOGGER.get("'stem': '{0}'".format(self._stem))
        return self._stem

    def _set_stem(self, stem):
        """
        Update the value of self._stem.

        :param stem:
        :type stem: str
        :return:
        """
        self._stem = stem
        LOGGER.set("'stem': '{0}'".format(self._stem))

    stem = property(fget=_get_stem, fset=_set_stem,
                    doc="The stem for this Word object.")

    def _get_chunk(self):
        """
        Get the current value of self._chunk.

        :return: str
        """
        LOGGER.get("'chunk': '{0}'".format(self._chunk))
        return self._chunk

    def _set_chunk(self, chunk):
        """
        Update the value of self._chunk.

        :param chunk:
        :type chunk: str
        :return:
        """
        self._chunk = chunk
        LOGGER.set("'chunk': '{0}'".format(self._chunk))

    chunk = property(fget=_get_chunk, fset=_set_chunk,
                     doc="The chunk for this Word object.")

    def _get_lemma(self):
        """
        Get the current value of self._lemma.

        :return: str
        """
        LOGGER.get("'lemma': '{0}'".format(self._lemma))
        return self._lemma

    def _set_lemma(self, lemma):
        """
        Update the value of self._lemma.

        :param lemma:
        :type lemma: str
        :return:
        """
        self._lemma = lemma
        LOGGER.set("'lemma': '{0}'".format(self._lemma))

    lemma = property(fget=_get_lemma, fset=_set_lemma,
                     doc="The lemma for this Word object.")

    def _get_syllables(self):
        """
        Get the current value of self._syllables.

        :return: int
        """
        LOGGER.get("'syllables': '{0}'".format(self._syllables))
        return self._syllables

    def _set_syllables(self, syllables):
        """
        Update the value of self._syllables.

        :param syllables:
        :type syllables: int
        :return:
        """
        self._syllables = syllables
        LOGGER.set("'syllables': '{0}'".format(self._syllables))

    syllables = property(fget=_get_syllables, fset=_set_syllables,
                         doc="The number of syllables in this Word object.")
    
    def _get_uncertainty(self):
        """
        Get the current value of self._uncertainty.

        :return: str
        """
        LOGGER.get("'uncertainty': '{0}'".format(self._uncertainty))        
        return self._uncertainty
    
    def _set_uncertainty(self, uncertainty):
        """
        Update the value of self._uncertainty.

        :param uncertainty:
        :type uncertainty: str
        :return:
        """
        if uncertainty in UNCERTAINTY_MAP.keys():    
            uncertainty = UNCERTAINTY_MAP[uncertainty]
        elif uncertainty in UNCERTAINTY_MAP.values():
            pass
                        
        if uncertainty in UNCERTAINTY_MAP.values():
            self._uncertainty = uncertainty
            LOGGER.set("'uncertainty': '{0}'".format(self._uncertainty))
        else:
            LOGGER.error("Received invalid 'uncertainty' label '{0}'."
                         .format(uncertainty))
        
    uncertainty = property(fget=_get_uncertainty, fset=_set_uncertainty,
                           doc="The uncertainty classification this word.")

    def __str__(self):
        """
        Get the str representation of this Word object.

        :return: str
        """
        return str(self.__dict__)

    def __dict__(self):
        """
        Get the dict representation of this Word object.

        :return: dict
        """
        d = {'word': self._word, 'pos': self._pos, 'stem': self._stem,
             'chunk': self._chunk, 'lemma': self._lemma,
             'syllables': self._syllables, 'uncertainty': self._uncertainty}
        return d
