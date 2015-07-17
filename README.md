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
## Release 1.0 Notes
* The application is now fully integrated with bash, removing some nasty reimplementing of code from previous versions.
* The provided functionality is far from complete; more will be coming, hopefully soon!

- - - -
## System Requirements
Currently, CLAAP has only been tested on 64-bit Ubuntu 15.04 with Python 2.7.9. 

- - - -
## Installation
Ensure that Python is installed on your machine.

Run the following in a command line.
    
    bash install

- - - -
## Execution

    claap COMMAND arg1 arg2 arg3 ...

- - - -
## Project Goals
* ``` ✓ ``` Develop a command-line interface.
* ``` _ ``` Provide basic metric gathering features.
* ``` _ ``` Provide basic annotation insertion features.
* ``` ✓ ``` Create a script for installing dependencies.
* ``` ✓ ``` Integrate with the bash shell.
* ``` ✓ ``` Integrate features from the Berkeley Parser.
* ``` _ ``` Port for Mac OS X.
* ``` _ ``` Port for Windows 7+.

- - - -
## Acknowledgments
I would like to thank Emily Prud'hommeaux and Cissi Ovesdotter-Alm for their guidance during my initial development process. I would also like to thank Bryan Meyers, my brother, letting me bounce ideas off of him, and for giving me wake-up calls when I was doing something in the less-than-intelligent (stupid) way.

&nbsp;&nbsp;&nbsp;&nbsp;Emily Tucker Prud'hommeaux < <emilypx@rit.edu> > < [CLaSP](http://www.rit.edu/clasp/people.html) >

&nbsp;&nbsp;&nbsp;&nbsp;Cissi Ovesdotter-Alm < <coacla@rit.edu> > < [CLaSP](http://www.rit.edu/clasp/people.html) >

&nbsp;&nbsp;&nbsp;&nbsp;Bryan T. Meyers < <btm5529@rit.edu> > < [DataDrake](http://www.datadrake.com/) > < [GitHub](https://github.com/DataDrake) >

- - - -
## Licensing
The files listed below are part of the [Berkeley Parser](https://github.com/slavpetrov/berkeleyparser):
* BerkeleyParser-1.7.jar
* eng_sm6.gr

For questions regarding the Berkeley Parser, please contact Slav Petrov < <petrov@cs.berkeley.edu> >.
