#!/usr/bin/env python

""" Defines objects/constants for the splat.chunkers module. """

__author__ = "Benjamin S. Meyers"
__copyright__ = "Copyright 2015-2017, Benjamin S. Meyers"
__credits__ = ["Benjamin S. Meyers"]
__version__ = "1.0.0"
__maintainer__ = "Benjamin S. Meyers"
__email__ = "ben@splat-library.org"
__status__ = "Development"

#### IMPORTS ###################################################################
from splat.chunkers import (chunker, chunker_conll2000, chunker_treebank)

Conll2000Chunker = chunker_conll2000.Conll2000Chunker()
TreebankChunker = chunker_treebank.TreebankChunker()


