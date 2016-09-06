#!/usr/bin/env python3

##### PYTHON IMPORTS ###################################################################################################
import os, pickle

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

curr_dir = os.path.dirname(__file__)
Google20K = pickle.load(open(curr_dir + '/google-20000-corpus.pkl', 'rb'))
EOWL = pickle.load(open(curr_dir + '/eowl-corpus.pkl', 'rb'))
Brown = pickle.load(open(curr_dir + '/brown-corpus.pkl', 'rb'))
Gutenberg = pickle.load(open(curr_dir + '/gutenberg-corpus.pkl', 'rb'))
Stopwords = pickle.load(open(curr_dir + '/stopwords-corpus.pkl', 'rb'))