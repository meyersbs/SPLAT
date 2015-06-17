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
