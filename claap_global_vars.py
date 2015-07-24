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
                'yngve':        'Get Yngve Score',                      'frazier':      'Get Frazier Score',
                'ism':          'Insert Speaker Markers',               'iqm':          'Insert Dialog Act Markers',
                'rsm':          'Remove Speaker Markers',               'rqm':          'Remove Dialog Act Markers',
                'iub':          'Insert Utterance Boundaries',          'rub':          'Remove Utterance Boundaries'}

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
                'yngve':        '\t\tfilename\t--', 'frazier':          '\t\tfilename\t--',
                'ism':          '\t\tfilename\t*output', 'iqm':              '\t\tfilename\t*output',
                'rsm':          '\t\tfilename\t*output', 'rqm':              '\t\tfilename\t*output',
                'iub':          '\t\tfilename\t*output', 'rub':              '\t\tfilename\t*output'}

dialog_act_dict = {1:       'Info-Request',             2:      'Action-Request',
                   3:       'Yes-Answer',               4:      'No-Answer',
                   5:       'Answer',                   6:      'Offer',
                   7:       'Report-On-Action',         8:      'Inform',
                   9:       'Greet',                    10:     'Quit',
                   11:      'Apology',                  12:     'Thank',
                   13:      'Clarification-Request',    14:     'Ack',
                   15:      'Filler',                   16:     'Other'}

dialog_acts = ' 1\t' + dialog_act_dict[1] + '\t\t 2\t' + dialog_act_dict[2] + '\n'
dialog_acts+= ' 3\t' + dialog_act_dict[3] + '\t\t 4\t' + dialog_act_dict[4] + '\n'
dialog_acts+= ' 5\t' + dialog_act_dict[5] + '\t\t\t 6\t' + dialog_act_dict[6] + '\n'
dialog_acts+= ' 7\t' + dialog_act_dict[7] + '\t 8\t' + dialog_act_dict[8] + '\n'
dialog_acts+= ' 9\t' + dialog_act_dict[9] + '\t\t\t10\t' + dialog_act_dict[10] + '\n'
dialog_acts+= '11\t' + dialog_act_dict[11] + '\t\t\t12\t' + dialog_act_dict[12] + '\n'
dialog_acts+= '13\t' + dialog_act_dict[13] + '\t14\t' + dialog_act_dict[14] + '\n'
dialog_acts+= '15\t' + dialog_act_dict[15] + '\t\t\t16\t' + dialog_act_dict[16] + '\n'

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
########################################################################################################################
