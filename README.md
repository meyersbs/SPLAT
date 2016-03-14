# SPLAT
## Speech Processing \& Linguistic Analysis Tool

- - - -
## Contact Information
&nbsp;&nbsp;&nbsp;&nbsp;Benjamin S. Meyers < <bsm9339@rit.edu> >

- - - -
## Project Description
SPLAT is a command-line application designed to make it easy for linguists (both computer-oriented and non-computer-oriented) to use the [Natural Language Tool Kit](http://www.nltk.org/) (NLTK) for analyzing virtually any text file.

SPLAT is designed to help you gather linguistic features from text files and it is assumed that most input files will not be already annotated. In order for SPLAT to function properly, you should ensure that the input files that you provide do not contain any annotations. Because there are so many variations of linguistic annotation schemes, it would simply be impossible to account for all of them in the initial parsing of input files; it is easier for you to remove any existing annotations than it is for me to do so.

- - - -
## System Requirements
SPLAT is being developed and tested on 64-bit Ubuntu 15.10 with Python 3.4.3. Minimum requirements include:
* Python 3.4 or Later
* NLTK 3.1 or Later
* Java (for the Berkeley Parser)

- - - -
## Installation
1. Ensure that Python is installed on your machine.
2. Download the install file: [install](/install)
3. Run the following in a command line:
``` bash
    chmod +x path/to/install
    ./path/to/install
```

To uninstall run the following in a command line.
```bash
    rm -rf ~/.SPLAT
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
    splat yngve filename            # (UNDER REVIEW) Calculate Yngve-Score
    splat frazier filename          # (UNDER REVIEW) Calculate Frazier-Score
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
## Release Notes
#### UPDATE
SPLAT is taking a new direction. NLTK, while not maintained too well, is still the best at what it does. Since I do not have the background to do everything that NLTK does, I will work on having SPLAT complement NLTK, rather than replace it.

#### Release 3.0
* SPLAT has been reorganized into packages so that it can either be used as a Python library, or as a command-line tool.
* The command-line interface has been cleaned up, and hopefully looks better.
* Dependencies on non-standard libraries have been greatly reduced.
  * NLTK is a requirement for frequency distributions and Tree structures. This will hopefully change soon.
  * The Berkeley Parser has been packaged with SPLAT in order for parse trees to be generated. This is likely a permanent dependency. 
* SPLAT functions have been optimized to increase efficiency and User satisfaction.

#### Release 2.0
* The Berkeley Parser and NLTK have been integrated with the application.
* The provided functionality is, for the most part, complete - that is, there isn't much more I plan to add at this time.

#### Release 1.0
* The application is now fully integrated with bash, removing some nasty reimplementing of code from previous versions.
* The provided functionality is far from complete; more will be coming, hopefully soon!

- - - -
## Acknowledgments
I would like to thank Emily Prud'hommeaux and Cissi Ovesdotter-Alm for their guidance during my initial development process. I would also like to thank Bryan Meyers, my brother, letting me bounce ideas off of him, and for giving me wake-up calls when I was doing something in the less-than-intelligent (stupid) way.
* Emily Tucker Prud'hommeaux < <emilypx@rit.edu> > < [CLaSP](http://www.rit.edu/clasp/people.html) >
* Cissi Ovesdotter-Alm < <coacla@rit.edu> > < [CLaSP](http://www.rit.edu/clasp/people.html) >
* Bryan T. Meyers < <bmeyers@datadrake.com> > < [DataDrake](http://www.datadrake.com/) > < [GitHub](https://github.com/DataDrake) >

- - - -
## Licensing
See [LICENSE.md](/LICENSE.md).
