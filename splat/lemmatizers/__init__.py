#!/usr/bin/env python

""" Defines objects/constants for the splat.lemmatizers module. """

__author__ = "Benjamin S. Meyers"
__copyright__ = "Copyright 2015-2017, Benjamin S. Meyers"
__credits__ = ["Benjamin S. Meyers"]
__version__ = "1.0.0"
__maintainer__ = "Benjamin S. Meyers"
__email__ = "ben@splat-library.org"
__status__ = "Development"

#### IMPORTS ###################################################################
from splat.lemmatizers import (lemmatizer, lemmatizer_wordnet)

WordNetLemmatizer = lemmatizer_wordnet.WordNetLemmatizer()
