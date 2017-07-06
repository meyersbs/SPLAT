#!/usr/bin/env python

""" Defines a chunker using nltk.corpus.treebank_chunk. """

__author__ = "Benjamin S. Meyers"
__copyright__ = "Copyright 2015-2017, Benjamin S. Meyers"
__credits__ = ["Benjamin S. Meyers"]
__version__ = "1.0.0"
__maintainer__ = "Benjamin S. Meyers"
__email__ = "ben@splat-library.org"
__status__ = "Development"

#### IMPORTS ###################################################################
from splat.chunkers import chunker
from nltk.corpus import treebank_chunk
from nltk.tag import UnigramTagger, BigramTagger


class TreebankChunker(chunker.Chunker):
    """ Implement splat.chunkers.chunker interface. """
    def __init__(self):
        """ Instantiate TreebankChunker object. """
        super(TreebankChunker, self).__init__()
        self._chunk_sents = self.tag_chunks(treebank_chunk.chunked_sents())
        self._tagger = BigramTagger(self._chunk_sents,
                                    backoff=UnigramTagger(self._chunk_sents))

    def chunk(self, pos_tags):
        """
        Determine chunks for each of the given part-of-speech tags.

        :param pos_tags:
        :type pos_tags: list
        :return: list
        """
        chunks = self._tagger.tag(pos_tags)
        return [chunk[1] for chunk in chunks]
