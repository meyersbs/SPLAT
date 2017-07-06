#!/usr/bin/env python

""" Defines a Chunker interface. """

__author__ = "Benjamin S. Meyers"
__copyright__ = "Copyright 2015-2017, Benjamin S. Meyers"
__credits__ = ["Benjamin S. Meyers"]
__version__ = "1.0.0"
__maintainer__ = "Benjamin S. Meyers"
__email__ = "ben@splat-library.org"
__status__ = "Development"

#### IMPORTS ###################################################################
from nltk.chunk import ChunkParserI
from nltk.chunk import tree2conlltags as to_tags


class Chunker(ChunkParserI):
    def __init__(self):
        raise NotImplementedError("'Chunker' is an interface.")

    def chunk(self, pos_tags):
        raise NotImplementedError("'Chunker' is an interface.")

    @staticmethod
    def tag_chunks(chunk_sents):
        """
        Convert NLTK's chunk tag format to something more usable.

        :param chunk_sents:
        :return: list
        """
        return [
            [(t, c) for (w, t, c) in chunk_tags]
            for chunk_tags in [to_tags(tree) for tree in chunk_sents]
        ]
