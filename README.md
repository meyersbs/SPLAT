[![Build Status](https://travis-ci.org/meyersbs/SPLAT.svg?branch=master)](https://travis-ci.org/meyersbs/SPLAT) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE.md) [![codecov](https://codecov.io/gh/meyersbs/SPLAT/branch/master/graph/badge.svg)](https://codecov.io/gh/meyersbs/SPLAT)
 [![PyPI](https://img.shields.io/pypi/pyversions/SPLAT-library.svg?maxAge=2592000)](https://pypi.python.org/pypi/SPLAT-library/0.3.7) [![PyPI](https://img.shields.io/pypi/v/SPLAT-library.svg?maxAge=2592000)](https://pypi.python.org/pypi/SPLAT-library/0.3.7) [![Website](https://img.shields.io/website-up-down-green-red/http/splat-library.org.svg?maxAge=2592000)](http://splat-library.org/)

<img src="https://cdn.rawgit.com/meyersbs/SPLAT/master/logo.svg" width="20%">
<br>
<img src="https://cdn.rawgit.com/meyersbs/SPLAT/master/tag.svg" width="60%">

- - - -
## Contact Information
&nbsp;&nbsp;&nbsp;&nbsp;Benjamin S. Meyers < <ben@splat-library.org> >

- - - -
## Project Description
SPLAT is a command-line application designed to make it easy for linguists (both computer-oriented and non-computer-oriented) to use the [Natural Language Tool Kit](http://www.nltk.org/) (NLTK) for analyzing virtually any text file.

SPLAT is designed to help you gather linguistic features from text files and it is assumed that most input files will not be already annotated. In order for SPLAT to function properly, you should ensure that the input files that you provide do not contain any annotations. Because there are so many variations of linguistic annotation schemes, it would simply be impossible to account for all of them in the initial parsing of input files; it is easier for you to remove any existing annotations than it is for me to do so.

- - - -
## System Requirementsgit 
SPLAT is being developed and tested on 64-bit Ubuntu 15.10 with Python 3.4.3. Minimum requirements include:
* Python 3.4 or Later
* NLTK 3.1 or Later
* Java (for the Berkeley Parser)

- - - -
## Installation
1. Ensure that Python3.4 (or newer) is installed on your machine.
2. Run the following in a command line:
``` bash
    pip3 install SPLAT-library

    # Recommended, but not required.
    echo 'alias splat="splat-cli"' >> ~/.bashrc
    echo 'alias splat="splat-cli"' >> ~/.bash_profile
    source .bashrc
```

To uninstall run the following in a command line.
```bash
    pip3 uninstall SPLAT-library
```

- - - -
## General Commands
```bash
    splat --commands                # List all available commands
    splat --help                    # Provide helpful information
    splat --info                    # Display version and copyright information
    splat --usage                   # Display basic command line structure
    splat bubble filename           # Display the raw text from the file
```

- - - -
## Analysis Functionality \& Usage
#### Types \& Tokens
```bash
    splat tokens filename           # List all Tokens
    splat types filename            # List all Types
    splat ttr filename              # Calculate Type-Token Ratio
    splat wc filename               # Word Count (Token Count)
    splat uwc filename              # Unique Word Count (Type Count)
```
##### Parts-Of-Speech
```bash
    splat pos filename              # List Tokens with their Parts-Of-Speech
    splat poscounts filename        # List Part-Of-Speech Tags with their Frequencies
```
#### Syntactic Complexity
```bash
    splat cdensity filename         # Calculate Content-Density
    splat idensity filename         # Calculate Idea Density
    splat flesch filename           # Calculate Flesch Readability Ease
    splat kincaid filename          # Calculate Flesch-Kincaid Grade Level
    splat yngve filename            # Calculate Yngve-Score
    splat frazier filename          # Calculate Frazier-Score
```
#### Listing Content \& Function Words
```bash
    splat function filename         # List all Function Words
    splat content filename          # List all Content Words
    splat ufunction filename        # Unique Function Words
    splat ucontent filename         # Unique Content Words
    splat cfr filename              # Calculate Content-Function Ratio
```
#### Utterances \& Sentences
```bash
    splat utts filename             # List all Utterances
    splat sents filename            # List all Sentences
    splat alu filename              # Average Utterance Length
    splat als filename              # Average Sentence Length
    splat uttcount filename         # Utterance Count
    splat sentcount filename        # Sentence Count
    splat syllables filename        # Display Number of Syllables
    splat wpu filename              # List the Number of Words in each Utterance
    splat wps filename              # List the number of Words in each Sentence
```
#### Frequency Distributions
```bash
    splat mostfreq filename x       # List the x Most Frequent Words
    splat leastfreq filename x      # List the x Least Frequent Words
    splat plotfreq filename x       # Draw and Display a Frequency Graph
```
#### Disfluencies
```bash
    splat disfluencies filename     # Calculate various Disfluency Counts
    splat dpa filename              # List the Number of Disfluencies per each Dialog Act
    splat dpu filename              # List the Number of Disfluencies in each Utterance
    splat dps filename              # List the Number of Disfluencies in each Sentence
```
#### Syntactic Parsing
```bash
    splat trees filename            # List Parse-Tree Strings for each Utterance
    splat maxdepth filename         # Calculate Max Tree Depth
    splat drawtrees filename        # Draw Parse Trees
```
#### Language Modeling
```bash
    splat unigrams filename         # List all Unigrams
    splat bigrams filename          # List all Bigrams
    splat trigrams filename         # List all Trigrams
    splat ngrams filename n         # List all n-grams
```

- - - -
## Annotation Functionality \& Usage
```bash
    splat annotate filename         # Semi-Automatically annotate the Utterances
```

- - - -
## Acknowledgments
I would like to thank Emily Prud'hommeaux and Cissi Ovesdotter-Alm for their guidance during my initial development process. I would also like to thank Bryan Meyers, my brother, letting me bounce ideas off of him, and for giving me wake-up calls when I was doing something in the less-than-intelligent (stupid) way.

| Name | Email | Website | GitHub |
|-----|-----|-----|-----|
| Emily Prud'hommeaux | < <emilypx@rit.edu> > | < [CLaSP](http://www.rit.edu/clasp/people.html) > | |
| Cissi O. Alm | < <coacla@rit.edu> > | < [CLaSP](http://www.rit.edu/clasp/people.html) > | |
| Bryan T. Meyers | < <bmeyers@datadrake.com> > | < [DataDrake](http://www.datadrake.com/) > | < [GitHub](https://github.com/DataDrake) > |

- - - -
## Licensing
See [LICENSE.md](/LICENSE.md).
