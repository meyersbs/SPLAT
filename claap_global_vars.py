#!/usr/bin/python

from nltk.corpus import stopwords

##### GLOBAL VARIABLES #################################################################################################
versions = ['Version 1.00\t06-24-15\t04:24 PM UTC',
            'Version 0.10\t06-16-15\t11:29 AM UTC',
            'Version 0.00\t06-15-15\t03:55 PM UTC']
stopwords = stopwords.words('english')  # List of Function Words
disfluency_list = ['um', 'uh', 'ah', 'er', 'hm']
open_class_list = ['NN', 'NNS', 'NNP', 'NNPS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'JJ', 'JJR', 'JJS', 'RB',
                   'RBR', 'RBS', 'FW']
ignore_list = ['LS', 'SYM', 'UH', 'LBR', 'RBR', '-LBR-', '-RBR-', '$', '``', '"', '\'\'', '(', ')', '()', '( )',
               '\,', '\-\-', '\.', '\:', 'SBAR', 'SBARQ']
proposition_list = ['CC', 'CD', 'DT', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'JJ', 'JJR', 'JJS', 'RB', 'RBR',
                    'RBS', 'IN', 'CC', 'PDT', 'POS', 'PP$', 'PRP$', 'TO', 'WDT', 'WP', 'WPS', 'WRB']
pause_count = 0
break_count = 0
total_disfluencies = 0

command_info = {'alu':          'Get Average Utterance Length',         'disfluencies': 'Get Total Disfluency Count',
                'dpu':          'List Disfluency Count per Utterance',  'drawtrees':    'Draw Parse Trees',
                'lcw':          'List Content Words',                   'leastfreq':    'List Least Frequent Words',
                'lfw':          'List Function Words',                  'lucw':         'List Unique Function Words',
                'lufw':         'List Unique Function Words',           'maxdepth':     'Get Max Tree Depth',
                'mostfreq':     'List Most Frequent Words',             'normalize':    'Display Normalized Text',
                'numutts':      'Get Number of Utterances',             'parsetrees':   'Get Parse Tree Strings',
                'plotfreq':     'Graph Frequency Distribution',         'pos':          'Tag Parts of Speech',
                'poscounts':    'List Counts for Each POS',             'stats':        'List Various Statistics',
                'tokens':       'List All Tokens (words)',              'ttr':          'Get Type-Token Ratio',
                'types':        'List All Types (unique words)',        'utterances':   'List All Utterances',
                'uwc':          'Get Number of Tokens',                 'wc':           'Get Total Word Count',
                'wpu':          'List Words per Utterance',             '--commands':   'List Valid Commands',
                '--help':       'List Help Info',                       '--info':       'List Program Info',
                '--usage':      'List Usage Info',                      '--version':    'Get Program Version',
                '--multi':      'Run a Command Multiple Times',         'cfr':          'Get Content-Function Ratio',
                'idensity':     'Get Idea Density',                     'cdensity':     'Get Content Density',
                'yngve':        'Get Yngve Score',                      'frazier':      'Get Frazier Score'}

command_args = {'alu':          '\t\tfilename\t--', 'disfluencies':     '\tfilename\t--',
                'dpu':          '\t\tfilename\t--', 'drawtrees':        '\tfilename\t--',
                'lcw':          '\t\tfilename\t--', 'leastfreq':        '\tfilename\t*int',
                'lfw':          '\t\tfilename\t--', 'lucw':             '\t\tfilename\t--',
                'lufw':         '\t\tfilename\t--', 'maxdepth':         '\tfilename\t--',
                'mostfreq':     '\tfilename\t*int', 'normalize':        '\tfilename\t--',
                'numutts':      '\t\tfilename\t--', 'parsetrees':       '\tfilename\t--',
                'plotfreq':     '\tfilename\t*int', 'pos':              '\t\tfilename\t--',
                'poscounts':    '\tfilename\t--',   'stats':            '\t\tfilename\t--',
                'tokens':       '\t\tfilename\t--', 'ttr':              '\t\tfilename\t--',
                'types':        '\t\tfilename\t--', 'utterances':       '\tfilename\t--',
                'uwc':          '\t\tfilename\t--', 'wc':               '\t\tfilename\t--',
                'wpu':          '\t\tfilename\t--', '--commands':       '\t--\t\t--',
                '--help':       '\t\t--\t\t--',     '--info':           '\t\t--\t\t--',
                '--usage':      '\t\t--\t\t--',     '--version':        '\t--\t\t--',
                '--multi':      '\t\t--\t\t--',     'cfr':              '\t\tfilename\t--',
                'idensity':     '\tfilename\t--',   'cdensity':         '\tfilename\t--',
                'yngve':        '\t\tfilename\t--', 'frazier':          '\t\tfilename\t--'}
########################################################################################################################
