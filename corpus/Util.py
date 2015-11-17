#!/usr/bin/python

import sys, os
if sys.version_info <= (2, 7):	import cPickle as pkl
else:							import pickle as pkl

########################################################################################################################
##### INFORMATION ######################################################################################################
### @PROJECT_NAME:		SPLAT: Speech Processing and Linguistic Annotation Tool										 ###
### @VERSION_NUMBER:																								 ###
### @PROJECT_SITE:		github.com/meyersbs/SPLAT																     ###
### @AUTHOR_NAME:		Benjamin S. Meyers																			 ###
### @CONTACT_EMAIL:		bsm9339@rit.edu																				 ###
### @LICENSE_TYPE:																									 ###
########################################################################################################################
########################################################################################################################

# Each key is a word from the google-20000-english.txt file. Each key maps to a list containing
curr_dir = os.path.dirname(__file__)
Google20K = pkl.load(open(curr_dir + '/google-20000-corpus.pkl', 'rb'))
EOWL = pkl.load(open(curr_dir + '/eowl-corpus.pkl', 'rb'))
Brown = pkl.load(open(curr_dir + '/brown-corpus.pkl', 'rb'))
Gutenberg = pkl.load(open(curr_dir + '/gutenberg-corpus.pkl', 'rb'))
Stopwords = pkl.load(open(curr_dir + '/stopwords-corpus.pkl', 'rb'))