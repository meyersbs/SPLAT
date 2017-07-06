#!/usr/bin/env python

""" Defines a Lemmatizer interface. """

__author__ = "Benjamin S. Meyers"
__copyright__ = "Copyright 2015-2017, Benjamin S. Meyers"
__credits__ = ["Benjamin S. Meyers"]
__version__ = "1.0.0"
__maintainer__ = "Benjamin S. Meyers"
__email__ = "ben@splat-library.org"
__status__ = "Development"


class Lemmatizer(object):
    def __init__(self):
        raise NotImplementedError("'Lemmatizer' is an interface!")

    def lemmatize(self, tokens, pos_tags):
        raise NotImplementedError("'Lemmatizer' is an interface!")
