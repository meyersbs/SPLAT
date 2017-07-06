#!/usr/bin/env python

""" Defines a Parser interface. """

__author__ = "Benjamin S. Meyers"
__copyright__ = "Copyright 2015-2017, Benjamin S. Meyers"
__credits__ = ["Benjamin S. Meyers"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Benjamin S. Meyers"
__email__ = "ben@splat-library.org"
__status__ = "Development"


class Parser(object):
    def __init__(self):
        raise NotImplementedError("'Parser' is an interface!")

    def parse(self, sentence):
        raise NotImplementedError("'Parser' is an interface!")
