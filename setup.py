#!/usr/bin/python3.4

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

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE.md') as f:
    license = f.read()

setup(
    name='SPLAT',
    version='0.0.1',
    description='Speech Processing & Linguistic Analysis Tool',
    long_description=readme,
    author='Benjamin S. Meyers',
    author_email='ben@splat-library.org',
    url='https://github.com/meyersbs/SPLAT',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)