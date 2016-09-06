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

"""
This package contains the following files:
	[01] brown-corpus.pkl
			The Brown University Standard Corpus of Present-Day American English (or just Brown Corpus) was compiled in
			the 1960s by Henry Kucera and W. Nelson Francis at Brown University, Providence, Rhode Island as a general
			corpus (text collection) in the field of corpus linguistics. It contains 500 samples of English-language
			text, totaling roughly one million words, compiled from works published in the United States in 1961.
			Project Site: <http://clu.uni.no/icame/brown/bcm.html>
	[02] eowl-corpus.pkl
			This corpus was created using Ken Loge's English Open Word List.
			Project Site: <http://dreamsteep.com/projects/the-english-open-word-list.html>
	[03] google-20000-corpus.pkl
			This corpus was created using the 20,000 most common English words from the Google Trillion-Word Corpus.
			Project Site: <https://github.com/first20hours/google-10000-english>
	[04] gutenberg-corpus.pkl
			This corpus was created using the Gutenberg corpus available in NLTK.
			Project Site: <https://www.gutenberg.org/wiki/Gutenberg:Terms_of_Use>
	[05] stopwords-corpus.pkl
			This corpus was created using the Stopwords corpus available in NLTK.
			Project Site: <http://www.nltk.org/>
	[06] Util.py
			Loads the above corpora files so they can be used throughout the codebase.
"""