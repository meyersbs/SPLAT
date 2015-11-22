# SPLAT
## Speech Processing \& Linguistic Annotation Tool

- - - -
## NOTICE
SPLAT is currently undergoing a massive renovation to provide the following:
* higher efficiency
* ability to be imported as a python package
* cleaner command-line-interface
* minimal (hopefully none) dependency on outside libraries

- - - -
## Contact Information
&nbsp;&nbsp;&nbsp;&nbsp;Benjamin S. Meyers < <bsm9339@rit.edu> >

- - - -
## Project Description
SPLAT is a command-line application designed to make it easy for linguists (both computer-oriented and non-computer-oriented) to use the [Natural Language Tool Kit](http://www.nltk.org/) (NLTK) for analyzing virtually any text file.

SPLAT is designed to help you annotate text files and it is assumed that most input files will not be already annotated. In order for SPLAT to function properly, you should ensure that the input files that you provide do not contain any annotations. Because there are so many variations of linguistic annotation schemes, it would simply be impossible to account for all of them in the initial parsing of input files; it is easier for you to remove any existing annotations than it is for me to do so.

- - - -
## System Requirements
SPLAT is being developed and tested on 64-bit Ubuntu 15.10 with Python 3.4.3. Minimum requirements include:
* Python 3.4 or Later
* NLTK 3.1 or Later

- - - -
## Installation
Ensure that Python is installed on your machine.

Run the following in a command line.
``` bash
    cd /path/to/dir/SPLAT
    bash setup
    bash install
```

To uninstall run the following in a command line.
```bash
    cd /path/to/dir/SPLAT
    bash uninstall
```

- - - -
## General Commands
```bash
    splat --commands                # List all available commands
    splat --help                    # Provide helpful information
    splat --info                    # Display version and copyright information
    splat --usage                   # Display basic command line structure
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
#### Content \& Idea Density Calculation
```bash
    splat cdensity filename         # Calculate Content-Density
    splat idensity filename         # Calculate Idea Density
```
#### Yngve \& Frazier Scoring
(Currently Under Review)
```bash
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
    splat dpu filename              # List the Number of Disfluencies in each Utterance
    splat dps filename              # List the Number of Disfluencies in each Sentence
```
#### Parse Trees
```bash
    splat trees filename            # List Parse-Tree Strings for each Utterance
    splat maxdepth filename         # Calculate Max Tree Depth
    splat drawtrees filename        # Draw Parse Trees
```

#### N-Grams
```bash
    splat unigrams filename         # List all Unigrams
    splat bigrams filename          # List all Bigrams
    splat trigrams filename         # List all Trigrams
    splat ngrams filename n         # List all n-grams
```

#### Dialog Acts
```bash
    splat actstats filename         # List Word/Disfluency counts per Utterance per Act
```

- - - -
## Annotation Functionality \& Usage
#### Speaker Markers
```bash
    splat ism filename *outfile     # Insert Speaker Markers
    splat rsm filename *outfile     # Remove Speaker Markers
```
#### Quarteroni Dialog-Acts
```bash
    splat iqm filename *outfile     # Insert Dialog-Acts
    splat rqm filename *outfile     # Remove Dialog-Acts
```
#### Meyers Dialog-Acts
```bash
    splat imm filename *outfile     # Insert Meyers Dialog-Acts
    splat rmm filename *outfile     # Remove Meyers Dialog-Acts
```

#### Utterance Boundaries
```bash
    splat iub filename *outfile     # Insert Utterance Boundaries
    splat rub filename *outfile     # Remove Utterance Boundaries
```

- - - -
## Release Notes
#### Release 2.0
* The Berkeley Parser and NLTK have been integrated with the application.
* The provided functionality is, for the most part, complete - that is, there isn't much more I plan to add at this time.

#### Release 1.0
* The application is now fully integrated with bash, removing some nasty reimplementing of code from previous versions.
* The provided functionality is far from complete; more will be coming, hopefully soon!

- - - -
## Acknowledgments
I would like to thank Emily Prud'hommeaux and Cissi Ovesdotter-Alm for their guidance during my initial development process. I would also like to thank Bryan Meyers, my brother, letting me bounce ideas off of him, and for giving me wake-up calls when I was doing something in the less-than-intelligent (stupid) way.

&nbsp;&nbsp;&nbsp;&nbsp;Emily Tucker Prud'hommeaux < <emilypx@rit.edu> > < [CLaSP](http://www.rit.edu/clasp/people.html) >

&nbsp;&nbsp;&nbsp;&nbsp;Cissi Ovesdotter-Alm < <coacla@rit.edu> > < [CLaSP](http://www.rit.edu/clasp/people.html) >

&nbsp;&nbsp;&nbsp;&nbsp;Bryan T. Meyers < <bmeyers@datadrake.com> > < [DataDrake](http://www.datadrake.com/) > < 
[GitHub](https://github.com/DataDrake) >

- - - -
## Licensing
The files listed below are part of the [Berkeley Parser](https://github.com/slavpetrov/berkeleyparser):
* BerkeleyParser-1.7.jar
* eng_sm6.gr

For questions regarding the Berkeley Parser, please contact Slav Petrov < <petrov@cs.berkeley.edu> >.

The functions listed below were adapted from [this script](https://github.com/neubig/util-scripts/blob/96c91e43b650136bb88bbb087edb1d31b65d389f/syntactic-complexity.py):
* splat_functions.get_word_score(tree)
* splat_functions.is_sentence(value)
* splat_functions.calc_yngve_score(tree, parent)
* splat_functions.calc_frazier_score(tree, parent, parent_label)
* splat_functions.get_yngve_score(text_file)
* splat_functions.get_frazier_score(text_file)

Permission to use this script was granted by the code owner, Graham Neubig. For related questions, you may contact 
him via email < <neubig@is.naist.jp> > or you can visit his [website](http://www.phontron.com/index.php).
