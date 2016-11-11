#!/usr/bin/env python3

########################################################################################################################
##### INFORMATION ######################################################################################################
### @PROJECT_NAME:		SPLAT: Speech Processing and Linguistic Analysis Tool										 ###
### @VERSION_NUMBER:																								 ###
### @PROJECT_SITE:		github.com/meyersbs/SPLAT																     ###
### @AUTHOR_NAME:		Benjamin S. Meyers																			 ###
### @CONTACT_EMAIL:		ben@splat-library.org																		 ###
### @LICENSE_TYPE:		MIT																							 ###
########################################################################################################################
########################################################################################################################

from nltk.corpus import brown
from nltk.corpus import stopwords
from nltk.corpus import names
from nltk.corpus import cmudict

# The Brown University Standard Corpus of Present-Day American English (or just Brown Corpus) was compiled in the 1960s
# by Henry Kucera and W. Nelson Francis at Brown University, Providence, Rhode Island as a general corpora (text
# collection) in the field of corpora linguistics. It contains 500 samples of English-language text, totaling roughly
# one million words, compiled from works published in the United States in 1961. Project Site:
# <http://clu.uni.no/icame/brown/bcm.html>
BROWN = brown
BROWN_TAGS = dict(brown.tagged_words())

# This is the Stopwords corpus available in NLTK. Project Site: <http://www.nltk.org/>
STOPWORDS_EN = stopwords.words('english')

# This is the Names corpus available in NLTK. Project Site: <http://www.nltk.org/>
PROPER_NAMES = names.words()

# This is v6.0 of the Carnegie-Mellon Pronouncing Dictionary (cmudict) available in NLTK. Project Site:
# <http://www.nltk.org/>
CMUDICT = cmudict.dict()

PHONEME_DICT = {"vow":  ["AA", "AA0", "AA1", "AA2", "AE", "AE0", "AE1", "AE2",
                         "AH", "AH0", "AH1", "AH2", "OA", "OA0", "OA1", "OA2",
                         "AW", "AW0", "AW1", "AW2", "AY", "AY0", "AY1", "AY2",
                         "EH", "EH0", "EH1", "EH2", "ER", "ER0", "ER1", "ER2",
                         "EY", "EY0", "EY1", "EY2", "IH", "IH0", "IH1", "IH2",
                         "IY", "IY0", "IY1", "IY2", "OW", "OW0", "OW1", "OW2",
                         "OY", "OY0", "OY1", "OY2", "UH", "UH0", "UH1", "UH2",
                         "UW", "UW0", "UW1", "UW2"
                        ],
                "con":  ["B", "CH", "D", "DH", "F", "G", "HH", "JH", "K", "K",
                         "L", "M", "N", "NG", "P", "R", "S", "SH", "T", "TH",
                         "V", "W", "Y", "Z", "ZH"
                        ]
                }
