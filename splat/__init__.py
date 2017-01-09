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
    from nltk import pos_tag
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
except ImportError:
    print("Oops! It looks like some essential NLTK data was not downloaded. Let's fix that.")
    print("Downloading 'stopwords' from NLTK ...")
    status = subprocess.call(["python3", "-m", "nltk.downloader", "stopwords"],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if status == 0:
        print("NLTK data 'stopwords' was successfully downloaded!")
    else:
        print("Hmm... I couldn't download the essential NLTK data for you. I suggest running this command:\n\tpython3"
              "-m nltk.downloader stopwords")

try:
    from nltk.corpus import names
except ImportError:
    print("Oops! It looks like some essential NLTK data was not downloaded. Let's fix that.")
    print("Downloading 'names' from NLTK ...")
    status = subprocess.call(["python3", "-m", "nltk.downloader", "names"],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if status == 0:
        print("NLTK data 'names' was successfully downloaded!")
    else:
        print("Hmm... I couldn't download the essential NLTK data for you. I suggest running this command:\n\tpython3"
              "-m nltk.downloader names")

try:
    from nltk.corpus import cmudict
except ImportError:
    print("Oops! It looks like some essential NLTK data was not downloaded. Let's fix that.")
    print("Downloading 'cmudict' from NLTK ...")
    status = subprocess.call(["python3", "-m", "nltk.downloader", "cmudict"],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if status == 0:
        print("NLTK data 'cmudict' was successfully downloaded!")
    else:
        print("Hmm... I couldn't download the essential NLTK data for you. I suggest running this command:\n\tpython3"
              "-m nltk.downloader cmudict")

try:
    from nltk.corpus import brown
except ImportError:
    print("Oops! It looks like some essential NLTK data was not downloaded. Let's fix that.")
    print("Downloading 'brown' from NLTK ...")
    status = subprocess.call(["python3", "-m", "nltk.downloader", "brown"],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if status == 0:
        print("NLTK data 'brown' was successfully downloaded!")
    else:
        print("Hmm... I couldn't download the essential NLTK data for you. I suggest running this command:\n\tpython3"
              "-m nltk.downloader brown")

try:
    from nltk.tokenize import punkt
except ImportError:
    print("Oops! It looks like some essential NLTK data was not downloaded. Let's fix that.")
    print("Downloading 'punkt' from NLTK ...")
    status = subprocess.call(["python3", "-m", "nltk.downloader", "punkt"],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if status == 0:
        print("NLTK data 'punkt' was successfully downloaded!")
    else:
        print("Hmm... I couldn't download the essential NLTK data for you. I suggest running this command:\n\tpython3"
              "-m nltk.downloader punkt")

try:
    #from nltk.corpus import averaged_perceptron_tagger
    from nltk.tag import PerceptronTagger
except ImportError:
    print("Oops! It looks like some essential NLTK data was not downloaded. Let's fix that.")
    print("Downloading 'averaged_perceptron_tagger' from NLTK ...")
    status = subprocess.call(["python3", "-m", "nltk.downloader", "averaged_perceptron_tagger"],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if status == 0:
        print("NLTK data 'averaged_perceptron_tagger' was successfully downloaded!")
    else:
        print("Hmm... I couldn't download the essential NLTK data for you. I suggest running this command:\n\tpython3"
              "-m nltk.downloader averaged_perceptron_tagger")

try:
    import matplotlib
except ImportError:
    print("Oops! It looks like matplotlib was not installed. Let's fix that.")
    print("Installing matplotlib...")
    status = subprocess.call(["pip3", "install", "matplotlib"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if status == 0:
        print("matplotlib was successfully installed!")
    else:
        print("Hmm... I couldn't install matplotlib for you. You probably don't have root privileges. I suggest running"
              "this command:\n\tsudo pip3 install matplotlib")

java_status = subprocess.call(["which", "java"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if java_status != 0:
    print("Java is not installed on your system. Java needs to be installed in order for me to do any part-of-speech"
          "tagging.\n\nPlease install java and try again.")
