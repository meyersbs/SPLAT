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

try:
    import nltk
    from splat.SPLAT import SPLAT
    nltk.download("stopwords")
    nltk.download("names")
    nltk.download("punkt")
    nltk.download("averaged_perceptron_tagger")
except:
    print(
        "WARNING: Essential NLTK data could not be installed. Please run the following:\n pip3 -m nltk.downloader stopwords names punkt averaged_perceptron_tagger")
