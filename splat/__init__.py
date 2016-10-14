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
import subprocess

try:
    import nltk
except ImportError:
    print("Oops! It looks like NLTK was not installed. Let's fix that.")
    print("Installing NLTK...")
    status = subprocess.call(["pip3", "install", "nltk"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if status == 0:
        print("NLTK was successfully installed!")
    else:
        print("Hmm... I couldn't install NLTK for you. You probably don't have root privileges. I suggest running this command:\n\tsudo pip3 install nltk")

try:
    from nltk.corpus import stopwords
    from nltk.corpus import names
    from nltk.tokenize import punkt
    from nltk import pos_tag
except ImportError:
    print("Oops! It looks like some essential NLTK was not downloaded. Let's fix that.")
    print("Downloading NLTK data...")
    status = subprocess.call(["python3", "-m", "nltk.downloader", "stopwords", "names", "punkt", "averaged_perceptron_tagger"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if status == 0:
        print("Essential NLTK data was successfully downloaded!")
    else:
        print("Hmm... I couldn't download the essential NLTK data for you. I suggest running this command:\n\tpython3 -m nltk.downloader stopwords names punkt averaged_perceptron_tagger")

try:
    import matplotlib
except ImportError:
    print("Oops! It looks like matplotlib was not installed. Let's fix that.")
    print("Installing matplotlib...")
    status = subprocess.call(["pip3", "install", "matplotlib"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if status == 0:
        print("matplotlib was successfully installed!")
    else:
        print("Hmm... I couldn't install matplotlib for you. You probably don't have root privileges. I suggest running this command:\n\tsudo pip3 install matplotlib")

try:
    import jsonpickle
except ImportError:
    print("Oops! It looks like jsonpickle was not installed. Let's fix that.")
    print("Installing jsonpickle...")
    status = subprocess.call(["pip3", "install", "jsonpickle"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if status == 0:
        print("jsonpickle was successfully installed!")
    else:
        print("Hmm... I couldn't install jsonpickle for you. You probably don't have root privileges. I suggest running this command:\n\tsudo pip3 install jsonpickle")

java_status = subprocess.call(["which", "java"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if java_status != 0:
    print("Java is not installed on your system. Java needs to be installed in order for me to do any part-of-speech tagging.\n\nPlease install java and try again.")