#!/usr/bin/env python

""" Defines objects/constants for the splat.classifiers module. """

__author__ = "Benjamin S. Meyers"
__copyright__ = "Copyright 2015-2017, Benjamin S. Meyers"
__credits__ = ["Benjamin S. Meyers"]
__version__ = "1.0.0"
__maintainer__ = "Benjamin S. Meyers"
__email__ = "ben@splat-library.org"
__status__ = "Development"

#### IMPORTS ###################################################################
from politeness.classifier import Classifier as p_classifier
from uncertainty.classifier import Classifier as u_classifier

PolitenessClassifier = p_classifier()
UncertaintyClassifier = u_classifier('word', binary=False)
