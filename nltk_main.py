#################################################################
# File Name: nltk_main.py					#
# Date Created: 06-16-2015					#
# Date Revised: 06-17-2015					#
# Author: Benjamin S. Meyers					#
# Email: bsm9339@rit.edu					#
# 	Advisor: Emily Prud'hommeaux				#
# 	Email: emilypx@rit.edu					#
# 	Advisor: Cissi Ovesdotter-Alm				#
# 	Email: coagla@rit.edu					#
#################################################################
from nltk_functions import *
from nltk_variables import *
from nltk_tests import run_tests

##### MAIN ######################################################
def main():
	print(startup_info)
	while(True):
		user_command = raw_input('Please provide a command: ')
		command = word_tokenize(user_command)
		#print(command)
		#print(get_lexical_diversity('moby_dick.txt'))
		#print(get_word_count('moby_dick.txt'))
		if command[0] == 'tk' and len(command) == 2:
			print(get_tokens(command[1]))
		elif command[0] == 'ty' and len(command) == 2:
			print(get_types(command[1]))
		elif command[0] == 'wc' and len(command) == 2:
			print(get_word_count(command[1]))
		elif command[0] == 'uwc' and len(command) == 2:
			print(get_unique_word_count(command[1]))
		elif command[0] == 'ld' and len(command) == 2:
			print(get_lexical_diversity(command[1]))
		elif command[0] == 'mf' and len(command) == 3:
			print(get_most_frequent(command[1], int(command[2])))
		elif command[0] == 'lf' and len(command) == 3:
			print(get_least_frequent(command[1], int(command[2])))
		elif command[0] == 's' and len(command) == 3:
			print(look_up_word(command[1], command[2]))
		elif command[0] == 'h' and len(command) == 1:
			display_command_list()
		elif command[0] == '!' and len(command) == 1:
			run_tests()
		elif command[0] == '~' and len(command) == 1:
			print(more_info)
		elif command[0] == '42' and len(command) == 1:
			print(douglas)
		elif command[0] == 'quit' and len(command) == 1:
			print('\n' + random.choice(exit_messages) + '\n')
			break
		else:
			print(invalid_command)

if __name__ == "__main__":
    main()
