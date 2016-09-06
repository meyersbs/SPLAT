from distutils.core import setup

setup(
    name='SPLAT-library',
    version='0.1.2',
    description='Speech Processing & Linguistic Analysis Tool',
    long_description="SPLAT is a command-line application designed to make it easy for linguists (both computer-oriented and non-computer-oriented) to use the Natural Language Tool Kit (NLTK) for analyzing virtually any text file. SPLAT is designed to help you gather linguistic features from text files and it is assumed that most input files will not be already annotated. In order for SPLAT to function properly, you should ensure that the input files that you provide do not contain any annotations. Because there are so many variations of linguistic annotation schemes, it would simply be impossible to account for all of them in the initial parsing of input files; it is easier for you to remove any existing annotations than it is for me to do so.",
    author='Benjamin S. Meyers',
    author_email='ben@splat-library.org',
    maintainer='Benjamin S. Meyers',
    maintainer_email='ben@splat-library.org',
    url='http://splat-library.org',
    download_url='https://github.com/meyersbs/SPLAT/tarball/0.1.2',
    requires=['matplotlib', 'nltk'],
    keywords=['nlp', 'natural language', 'natural language processing'],
    packages=['splat', 'splat.annotation', 'splat.base', 'splat.classify', 'splat.complexity', 'splat.corpus', 'splat.model', 'splat.parse', 'splat.sentenizers', 'splat.tag', 'splat.tokenizers']
)
