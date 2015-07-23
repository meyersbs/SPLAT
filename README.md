# CLAAP
## Corpus & Linguistics Annotating & Analyzing in Python

- - - -
## Contact Information
&nbsp;&nbsp;&nbsp;&nbsp;Benjamin S. Meyers < <bsm9339@rit.edu> >

- - - -
## Project Description
CLAAP is a command-line application designed to make it easy for linguists (both computer-oriented and non-computer-oriented) to use the [Natural Language Tool Kit](http://www.nltk.org/) (NLTK) for analyzing virtually any text file.

CLAAP is designed to help you annotate text files and it is assumed that most input files will not be already annotated. In order for CLAAP to function properly, you should ensure that the input files that you provide do not contain any annotations. Because there are so many variations of linguistic annotation schemes, it would simply be impossible to account for all of them in the initial parsing of input files; it is easier for you to remove any existing annotations than it is for me to do so.

- - - -
## System Requirements
Currently, CLAAP has only been tested on 64-bit Ubuntu 15.04 with Python 2.7.9. 

- - - -
## Installation
Ensure that Python is installed on your machine.

Run the following in a command line.
``` bash    
    bash install
```

- - - -
## Analysis Functionality \& Usage
#### Types \& Tokens
```bash
    claap tokens filename       # List all Tokens
    claap types filename        # List all Types
    claap ttr filename          # Calculate Type-Token Ratio
    claap wc filename           # Word Count (Token Count)
    claap uwc filename          # Unique Word Count (Type Count)
```
#### Content \& Idea Density Calculation
```bash
    claap cdensity filename     # Calculate Content-Density
    claap idensity filename     # Calculate Idea Density
```
#### Yngve \& Frazier Scoring
```bash
    claap yngve filename        # Calculate Yngve-Score
    claap frazier filename      # Calculate Frazier-Score
```
#### Listing Content \& Function Words
```bash
    claap lfw filename          # List all Function Words
    claap lcw filename          # List all Content Words
    claap lufw filename         # Unique Function Words
    claap lucw filename         # Unique Content Words
    claap cfr filename          # Calculate Content-Function Ratio
```
#### Utterances
```bash
    claap utterances filename   # List all Utterances
    claap alu filename          # Calculate Mean Length Utterance
    claap numutts filename      # Utterance Count
    claap wpu filename          # List the Number of Words in each Utterance
```
#### Frequency Distributions
```bash
    claap mostfreq filename x   # List the x Most Frequent Words
    claap leastfreq filename x  # List the x Least Frequent Words
    claap plotfreq filename x   # Draw and Display a Frequency Graph
```
#### Disfluencies
```bash
    claap disfluencies filename # Calculate various Disfluency Counts
    claap dpu filename          # List the Number of Disfluencies in each Utterance
```
#### Parse Trees
```bash
    claap parsetrees filename   # List Parse-Tree Strings for each Utterance
    claap maxdepth filename     # Calculate Max Tree Depth
    claap drawtrees filename    # Draw Parse Trees
```

- - - -
## Annotation Functionality \& Usage
#### Speaker Markers
```bash
    claap ism filename          # Insert Speaker Markers
    claap rsm filename          # Remove Speaker Markers
```
#### Quarteroni Dialog-Acts
```bash
    claap iqm filename          # Insert Dialog-Acts
    claap rqm filename          # Remove Dialog-Acts
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
* claap_functions.get_word_score(tree)
* claap_functions.is_sentence(value)
* claap_functions.calc_yngve_score(tree, parent)
* claap_functions.calc_frazier_score(tree, parent, parent_label)
* claap_functions.get_yngve_score(text_file)
* claap_functions.get_frazier_score(text_file)

Permission to use this script was granted by the code owner, Graham Neubig. For related questions, you may contact 
him via email < <neubig@is.naist.jp> > or you can visit his [website](http://www.phontron.com/index.php).
