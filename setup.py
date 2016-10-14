from distutils.core import setup

setup(
    name='SPLAT-library',
    version='0.3.0',
    description='Speech Processing & Linguistic Analysis Tool',
    long_description="SPLAT is a command-line application designed to make it easy for linguists (both computer-oriented and non-computer-oriented) to use the Natural Language Tool Kit (NLTK) for analyzing virtually any text file.\n\nSPLAT is designed to help you gather linguistic features from text files and it is assumed that most input files will not be already annotated. In order for SPLAT to function properly, you should ensure that the input files that you provide do not contain any annotations. Because there are so many variations of linguistic annotation schemes, it would simply be impossible to account for all of them in the initial parsing of input files; it is easier for you to remove any existing annotations than it is for me to do so.",
    url='http://splat-library.org',
    author='Benjamin S. Meyers',
    author_email='ben@splat-library.org',
    license='MIT',
    scripts=['splat/splat'],
    keywords=['nlp', 'natural language', 'natural language processing'],
    package_data={'splat.parsers': ['BerkeleyParser-1.7.jar', 'eng_sm6.gr']},
    packages=[
        'splat',
        'splat.classifiers',
        'splat.complexity',
        'splat.corpora',
        'splat.gramminators',
        'splat.parsers',
        'splat.sentenizers',
        'splat.taggers',
        'splat.tokenizers'
    ],
    download_url='https://github.com/meyersbs/SPLAT/archive/v0.3.0.tar.gz',
    requires=['matplotlib', 'nltk', 'jsonpickle'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux'
    ]
)
