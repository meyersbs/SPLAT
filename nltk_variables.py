#################################################################
# File Name: nltk_variables.py					#
# Date Created: 06-17-2015					#
# Date Revised: 06-17-2015					#
# Author: Benjamin S. Meyers					#
# Email: bsm9339@rit.edu					#
# 	Advisor: Emily Prud'hommeaux				#
# 	Email: emilypx@rit.edu					#
# 	Advisor: Cissi Ovesdotter-Alm				#
# 	Email: coagla@rit.edu					#
#################################################################
from termcolor import *

##### GLOBAL VARIABLES ##########################################
startup_info = '#################################################################'
startup_info +='\n# CLAAP - Corpus & Linguistics Annotating & Analyzing in Python #'
startup_info +='\n# Version 0.00 \tJune 15, 2015 \t3:55 PM UTC \t\t\t#'
startup_info +='\n# Developed by Benjamin S. Meyers\t\t\t\t#'
startup_info +='\n#\t\t\t\t\t\t\t\t#'
startup_info +='\n# This application may not be copied, altered, or distributed \t#'
startup_info +='\n# without written consent from the product owner. \t\t#'
startup_info +='\n# \t\t\t\t\t\t\t\t#'
startup_info +='\n# Type '+ colored('~', 'green') +' for more information. \t\t\t\t\t#'
startup_info +='\n#\t\t\t\t\t\t\t\t#'
startup_info +='\n# Welcome to CLAAP! Type '+ colored('h', 'red') +' for help.\t\t\t\t#'
startup_info +='\n#################################################################'

exit_messages = [("If you're happy and you know it, CLAAP your hands!"),("Petrichor\n(noun)\na pleasant smell that frequently accompanies the first rain after a long period of warm, dry weather."), ("Syzygy is the only word in English that contains three 'y's."), ("Tmesis is the only word in the English language that begins with 'tm'."), ("In Old English, bagpipes were called 'doodle sacks'."), ("A 'quire' is two-dozen sheets of paper."), ("'Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo' is a grammatically correct sentence in American English."), ("J.R.R. Tolkien coined the term 'glossopoeia,' which is the act of inventing languages."), ("Beowulf is an English work, but if you try to read it in its original form, it will look like gibberish!"), ("'To Be Or Not To Be' = 'U+0032 U+0042 U+2228 U+0021 U+0032 U+0042'")]

more_info = "\nThis application was developed by Benjamin S. Meyers beginning on June 1, 2015 for an Undergraduate Research Internship at the Rochester Institute of Technology. CLAAP's primary application is to allow an easy-to-use tool for Linguists to annotate and analyze corpora consisting of discourse and dialogue.\n\tVersion 0.00\tJune 15, 2015\t3:55 PM UTC\n\tVersion 0.01\tJune 16, 2015\t11:29 AM UTC"

douglas = "\n           o o o   .-\'\"\"\"\'-.   o o o             DON\'T PANIC!"
douglas +="\n           \\\|/  .'         '.  \|//"
douglas +="\n            \-;o/             \o;-/"
douglas +="\n            // ;               ; \\\\"
douglas +="\n           //__; :.         .: ;__\\\\"
douglas +="\n          `-----\\'.'-.....-'.'/-----'           444    2222222"
douglas +="\n                 '.'.-.-,_.'.'                 4444   222   222"
douglas +="\n                   '(  (..-'                  44 44         22"
douglas +="\n      |              '-'                     44  44        22"
douglas +="\n  |           |                             444444444     22"
douglas +="\n |  |  |    |                                    44      22"
douglas +="\n     |     |  |                                  44    222"
douglas +="\n| |   |     %%%                                  44   222222222"
douglas +="\n    ___    _\|/_         _%%_____"
douglas +="\n\,-\' \'_|   \___/      __/___ \'   \\"                    
douglas +="\n/\"\"----\'          ___/__  \'   \'\'  \__%__       __%____%%%___"
douglas +="\n                 /   \" \'   _%__ \'   \'   \_____/____ \'  __ \" \\"
douglas +="\n           __%%_/__\'\' __     \'   _%_\'_   \     \"\'    _%__ \'\' \_"
douglas +="\n __/\__%%_/_/___\___ \'\'   \'_%_\"___   \"    \_%__ \'___\"     \"\'   \\"
douglas +="\n/_________________\____\'_RIP Douglas___\"_______\_______\'_____\"__\\"
douglas +="\n"

invalid_command = "Invalid Command. For help, type 'h'."
invalid_command+= "\nCommands should follow this form: " + colored('COMMAND', 'green') + " " + colored('Arg1', 'red') + " " + colored('Arg2', 'red')

lorem_ipsum_tokens = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetur', 'adipiscing', 'elit.', 'Maecenas', 'semper', 'nisl', 'fermentum', 'auctor', 'facilisis.', 'Pellentesque', 'vehicula', 'pharetra', 'leo,', 'ornare', 'vehicula', 'neque', 'cursus', 'id.', 'Maecenas', 'commodo', 'sapien', 'sed', 'purus', 'mollis', 'condimentum.', 'Nulla', 'ultricies', 'sapien', 'nec', 'urna', 'consectetur,', 'non', 'vulputate', 'elit', 'faucibus.', 'Nulla', 'in', 'luctus', 'arcu.', 'Nunc', 'sit', 'amet', 'accumsan', 'purus.', 'Donec', 'lectus', 'nulla,', 'aliquet', 'et', 'dui', 'in,', 'ullamcorper', 'tincidunt', 'nibh.', 'Duis', 'iaculis', 'mi', 'risus.', 'Phasellus', 'id', 'volutpat', 'ex,', 'a', 'imperdiet', 'diam.', 'Maecenas', 'eu', 'tellus', 'a', 'dui', 'ultricies', 'placerat.', 'Pellentesque', 'magna', 'nibh,', 'vulputate', 'et', 'elit', 'eget,', 'tristique', 'facilisis', 'tellus.', 'Aliquam', 'quis', 'neque', 'tortor.', 'Phasellus', 'vitae', 'elit', 'ut', 'ante', 'consequat', 'varius.', 'Mauris', 'ut', 'enim', 'velit.', 'Aliquam', 'et', 'dignissim', 'tellus.', 'Proin', 'sit', 'amet', 'maximus', 'lorem.', 'Vivamus', 'enim', 'nisi,', 'venenatis', 'eu', 'faucibus', 'eget,', 'dapibus', 'sed', 'justo.', 'Donec', 'ullamcorper', 'dolor', 'sed', 'nisi', 'volutpat,', 'at', 'venenatis', 'lacus', 'tempus.', 'Praesent', 'at', 'aliquet', 'justo.', 'Donec', 'aliquam', 'lectus', 'sed', 'convallis', 'eleifend.', 'Donec', 'vel', 'lectus', 'at', 'tellus', 'efficitur', 'imperdiet', 'volutpat', 'quis', 'nisl.', 'Praesent', 'tristique', 'sagittis', 'tortor', 'et', 'ultrices.', 'Aenean', 'vitae', 'sapien', 'sed', 'libero', 'convallis', 'ullamcorper', 'quis', 'a', 'lorem.', 'Integer', 'eget', 'consequat', 'lacus,', 'non', 'volutpat', 'quam.', 'Ut', 'nulla', 'massa,', 'mollis', 'ut', 'metus', 'eget,', 'volutpat', 'tincidunt', 'mi.', 'Vestibulum', 'varius', 'est', 'nec', 'mauris', 'euismod,', 'ac', 'imperdiet', 'eros', 'dictum.', 'Curabitur', 'finibus', 'elit', 'lorem,', 'ornare', 'semper', 'turpis', 'eleifend', 'ac.', 'Etiam', 'sit', 'amet', 'mollis', 'diam,', 'id', 'sodales', 'nisl.', 'Sed', 'et', 'sem', 'a', 'enim', 'ultricies', 'elementum', 'id', 'in', 'libero.', 'Pellentesque', 'habitant', 'morbi', 'tristique', 'senectus', 'et', 'netus', 'et', 'malesuada', 'fames', 'ac', 'turpis', 'egestas.', 'Morbi', 'non', 'mauris', 'non', 'mi', 'accumsan', 'ullamcorper', 'non', 'at', 'elit.', 'Aenean', 'euismod', 'urna', 'sed', 'sem', 'ultricies,', 'id', 'pretium', 'nibh', 'suscipit.', 'Nulla', 'porttitor', 'ante', 'ac', 'tortor', 'auctor', 'luctus.', 'Vestibulum', 'non', 'placerat', 'felis.', 'Maecenas', 'commodo', 'fringilla', 'arcu', 'id', 'commodo.', 'Donec', 'quis', 'pellentesque', 'est.', 'Etiam', 'lectus', 'mauris,', 'auctor', 'eu', 'condimentum', 'at,', 'dictum', 'ut', 'nulla.', 'Integer', 'sollicitudin', 'suscipit', 'velit', 'eu', 'tincidunt.', 'Morbi', 'id', 'nulla', 'id', 'nunc', 'fringilla', 'luctus.', 'Phasellus', 'posuere', 'justo', 'diam,', 'in', 'porta', 'libero', 'sodales', 'nec.', 'In', 'eget', 'nibh', 'sollicitudin,', 'malesuada', 'ex', 'vitae,', 'luctus', 'justo.', 'Nam', 'sit', 'amet', 'sem', 'a', 'quam', 'mollis', 'porta.', 'Proin', 'mattis', 'elit', 'eu', 'nibh', 'accumsan', 'fermentum', 'id', 'vitae', 'risus.', 'Nunc', 'vitae', 'enim', 'in', 'eros', 'rutrum', 'feugiat', 'eget', 'vitae', 'massa.', 'Donec', 'a', 'dolor', 'iaculis,', 'aliquet', 'justo', 'vitae,', 'bibendum', 'ipsum.', 'Cras', 'at', 'tellus', 'quis', 'ipsum', 'cursus', 'imperdiet', 'nec', 'non', 'tellus.', 'Suspendisse', 'auctor', 'mauris', 'in', 'consequat', 'sollicitudin.', 'In', 'hac', 'habitasse', 'platea', 'dictumst.', 'Aenean', 'ac', 'tellus', 'sed', 'felis', 'venenatis', 'pharetra.', 'Aliquam', 'gravida', 'elementum', 'tortor,', 'dapibus', 'dapibus', 'urna', 'lobortis', 'in.', 'Ut', 'lobortis', 'sapien', 'neque,', 'id', 'auctor', 'nulla', 'convallis', 'et.', 'Vivamus', 'lacinia', 'et', 'nisl', 'at', 'suscipit.', 'Phasellus', 'ultrices', 'velit', 'at', 'metus', 'volutpat', 'posuere.', 'Ut', 'laoreet,', 'magna', 'a', 'laoreet', 'sagittis,', 'enim', 'turpis', 'faucibus', 'lectus,', 'sit', 'amet', 'bibendum', 'leo', 'massa', 'id', 'ante.', 'Etiam', 'quam', 'ligula,', 'porttitor', 'a', 'nisi', 'vel,', 'fringilla', 'tincidunt', 'ante.', 'Maecenas', 'accumsan', 'turpis', 'sed', 'tincidunt', 'hendrerit.', 'Cras', 'at', 'nunc', 'ante.', 'Aenean', 'in', 'cursus', 'massa.']

lorem_ipsum_types = set(['Mauris', 'ipsum.', 'lacus', 'laoreet', 'ac.', 'elit', 'condimentum', 'volutpat,', 'egestas.', 'eros', 'laoreet,', 'ligula,', 'lacus,', 'hac', 'tellus', 'consectetur', 'lectus,', 'Donec', 'sapien', 'metus', 'non', 'nibh', 'tincidunt', 'bibendum', 'Morbi', 'nisi', 'consequat', 'purus.', 'malesuada', 'ultrices.', 'neque,', 'habitasse', 'faucibus', 'ipsum', 'neque', 'mattis', 'nisl', 'Phasellus', 'commodo.', 'porta', 'lacinia', 'tincidunt.', 'tempus.', 'suscipit.', 'ante.', 'ultricies,', 'Praesent', 'sollicitudin', 'posuere', 'auctor', 'enim', 'sagittis', 'tortor,', 'vitae,', 'tortor.', 'tellus.', 'sed', 'ex', 'hendrerit.', 'eu', 'et', 'sodales', 'mauris,', 'eget,', 'iaculis', 'est', 'arcu.', 'faucibus.', 'dictumst.', 'placerat.', 'sagittis,', 'mi.', 'nec', 'id.', 'Sed', 'nunc', 'sem', 'Curabitur', 'et.', 'mollis', 'Aliquam', 'suscipit', 'elementum', 'Ut', 'velit', 'leo', 'euismod,', 'justo.', 'euismod', 'magna', 'imperdiet', 'Nulla', 'nisi,', 'amet', 'aliquam', 'amet,', 'felis.', 'posuere.', 'justo', 'libero', 'senectus', 'facilisis', 'nulla', 'placerat', 'pharetra', 'ultrices', 'quam.', 'ac', 'purus', 'morbi', 'vel', 'venenatis', 'elit.', 'ante', 'dui', 'quis', 'pretium', 'fringilla', 'dictum.', 'nibh.', 'nibh,', 'porttitor', 'facilisis.', 'Integer', 'Maecenas', 'feugiat', 'luctus', 'Vestibulum', 'lobortis', 'eget', 'vehicula', 'leo,', 'nisl.', 'quam', 'consectetur,', 'efficitur', 'Pellentesque', 'iaculis,', 'Nam', 'accumsan', 'dapibus', 'Suspendisse', 'tortor', 'ut', 'ultricies', 'mi', 'vulputate', 'maximus', 'Aenean', 'Vivamus', 'volutpat', 'massa,', 'massa.', 'pharetra.', 'fames', 'Nunc', 'felis', 'luctus.', 'varius', 'dictum', 'Cras', 'semper', 'eleifend.', 'ornare', 'lectus', 'habitant', 'eleifend', 'Etiam', 'at', 'porta.', 'in', 'condimentum.', 'diam,', 'id', 'urna', 'nec.', 'mauris', 'risus.', 'varius.', 'vel,', 'sit', 'libero.', 'ex,', 'platea', 'netus', 'convallis', 'pellentesque', 'massa', 'diam.', 'dignissim', 'vitae', 'Lorem', 'arcu', 'commodo', 'gravida', 'est.', 'In', 'turpis', 'in,', 'in.', 'sollicitudin,', 'sollicitudin.', 'cursus', 'aliquet', 'nulla.', 'Proin', 'nulla,', 'a', 'lorem,', 'lorem.', 'rutrum', 'ullamcorper', 'tristique', 'Duis', 'adipiscing', 'dolor', 'finibus', 'fermentum', 'at,', 'velit.'])

lorem_ipsum_ttr = 48.57

lorem_ipsum_wc = 453

lorem_ipsum_uwc = 220

lorem_ipsum_mf30 = [('id', 10), ('sed', 8), ('et', 8), ('at', 8), ('a', 8), ('non', 7), ('Donec', 6), ('in', 6), ('sit', 6), ('elit', 5), ('auctor', 5), ('enim', 5), ('eu', 5), ('amet', 5), ('quis', 5), ('Maecenas', 5), ('volutpat', 5), ('vitae', 5), ('tellus', 4), ('sapien', 4), ('tincidunt', 4), ('Phasellus', 4), ('mollis', 4), ('imperdiet', 4), ('ac', 4), ('accumsan', 4), ('ut', 4), ('Aenean', 4), ('lectus', 4), ('turpis', 4)]

lorem_ipsum_lf30 = [('velit.', 1), ('at,', 1), ('finibus', 1), ('adipiscing', 1), ('Duis', 1), ('rutrum', 1), ('lorem,', 1), ('nulla,', 1), ('nulla.', 1), ('sollicitudin.', 1), ('sollicitudin,', 1), ('in.', 1), ('in,', 1), ('est.', 1), ('gravida', 1), ('arcu', 1), ('Lorem', 1), ('dignissim', 1), ('diam.', 1), ('massa', 1), ('pellentesque', 1), ('netus', 1), ('platea', 1), ('ex,', 1), ('libero.', 1), ('vel,', 1), ('varius.', 1), ('nec.', 1), ('condimentum.', 1), ('porta.', 1)]

lorem_ipsum_pos = {'VBG': 1, 'NN': 96, 'VBD': 2, 'CC': 1, 'JJS': 1, 'VBN': 2, '-NONE-': 12, 'VBP': 3, 'JJ': 5, 'IN': 3, 'VBZ': 14, 'DT': 1, 'NNS': 7, 'NNP': 72}

