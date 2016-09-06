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
	[01] CleanTokenizer.py
			Provides the functionality to tokenize a given text input, removing all punctuation before generating
			tokens.
	[02] PunctTokenizer.py
			Provides the functionality to tokenize a given text input, treating punctuation as separate tokens.
	[03] RawTokenizer.py
			Provides the functionality to tokenize a given text input with no pre-processing or normalizing.
	[04] Tokenizer.py
			An abstract class that is implemented by the other Tokenizers in this directory.
"""