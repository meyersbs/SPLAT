[![Build Status](https://travis-ci.org/meyersbs/SPLAT.svg?branch=master)](https://travis-ci.org/meyersbs/SPLAT) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE.md) [![codecov](https://codecov.io/gh/meyersbs/SPLAT/branch/master/graph/badge.svg)](https://codecov.io/gh/meyersbs/SPLAT)
 [![PyPI](https://img.shields.io/pypi/pyversions/SPLAT-library.svg?maxAge=2592000)](https://pypi.python.org/pypi/SPLAT-library/0.3.8) [![PyPI](https://img.shields.io/pypi/v/SPLAT-library.svg?maxAge=2592000)](https://pypi.python.org/pypi/SPLAT-library/0.3.8) [![Website](https://img.shields.io/website-up-down-green-red/http/splat-library.org.svg?maxAge=2592000)](http://splat-library.org/)

<img src="https://cdn.rawgit.com/meyersbs/SPLAT/master/docs/logo.svg" width="20%">
<br>
<img src="https://cdn.rawgit.com/meyersbs/SPLAT/master/docs/tag.svg" width="60%">

- - - -
## Contact Information
&nbsp;&nbsp;&nbsp;&nbsp;Benjamin S. Meyers <[ben@splat-library.org](mailto:ben@splat-library.org)>

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
1. Ensure that Python3.4 (or newer) is installed on your machine.
2. Run the following in a command line:
``` bash
    pip3 install SPLAT-library
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
    splat splat filename            # Display the raw text from the file
```

- - - -
## Functionality \& Usage

Coming Soon!

- - - -
## Acknowledgments

See [Acknowledgments](http://splat-library.org/#section5).

- - - -
## Licensing
See [LICENSE.md](/LICENSE.md).
