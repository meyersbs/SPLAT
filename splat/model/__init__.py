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
	[01] CaseNGramminator.py
			Provides functions to create ngrams. All characters in the given text are lowercased before ngrams are
			generated.
	[02] FullNGramminator.py
			Provides functions to create ngrams. Characters matching r"[\.,:;!\?\(\)\[\]\{\}]" are excluded from the
			ngram model. All characters in the given text are lowercased before ngrams are
			generated. This is essentially a combination of the PunctNGramminator and the CaseNGramminator.
	[03] NGramminator.py
			An abstract class implemented by the other NGramminators in this directory.
	[04] PunctNGramminator.py
			Provides functions to create ngrams. Characters matching r"[\.,:;!\?\(\)\[\]\{\}]" are excluded from the
			ngram model.
	[05] RawNGramminator.py
			Provides functions to create ngrams. No pre-processing or normalization of the text tokens takes place.
"""