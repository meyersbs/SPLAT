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

##### ALIASES ###################################################
file_aliases = build_alias_dict()

##### MAIN ######################################################
def main():
	print(startup_info)
	while(True):
		user_command = raw_input('Please provide a command: ')
		command = word_tokenize(user_command)
		#print(tag_parts_of_speech('test_words.txt'))
		#print(get_most_frequent('test_words.txt', -1))
		#print(get_pos_counts('test_words.txt'))
		#print(command)
		#print(get_lexical_diversity('moby_dick.txt'))
		#print(get_word_count('moby_dick.txt'))
		if command[0] == 'tk' and len(command) == 2:
			if file_aliases[command[1]] != None:
				print(get_tokens(file_aliases[command[1]]))
			else:
				print(get_tokens(command[1]))
		elif command[0] == 'ty' and len(command) == 2:
			if file_aliases[command[1]] != None:
				print(get_types(file_aliases[command[1]]))
			else:
				print(get_types(command[1]))
		elif command[0] == 'wc' and len(command) == 2:
			if file_aliases[command[1]] != None:
				print(get_word_count(file_aliases[command[1]]))
			else:
				print(get_word_count(command[1]))
		elif command[0] == 'uwc' and len(command) == 2:
			if file_aliases[command[1]] != None:
				print(get_unique_word_count(file_aliases[command[1]]))
			else:
				print(get_unique_word_count(command[1]))
		elif command[0] == 'ttr' and len(command) == 2:
			if file_aliases[command[1]] != None:
				print(str(get_TTR(file_aliases[command[1]])) + '%')
			else:
				print(str(get_TTR(command[1])) + '%')
		elif command[0] == 'pfd' and len(command) == 2:
			if file_aliases[command[1]] != None:
				plot_freq_dist(file_aliases[command[1]], -1)
			else:
				plot_freq_dist(command[1], -1)
		elif command[0] == 'pos' and len(command) == 2:
			if file_aliases[command[1]] != None:
				print(tag_parts_of_speech(file_aliases[command[1]]))
			else:
				print(tag_parts_of_speech(command[1]))
		elif command[0] == 'psc' and len(command) == 2:
			if file_aliases[command[1]] != None:
				print(get_pos_counts(file_aliases[command[1]]))
			else:
				print(get_pos_counts(command[1]))
		elif command[0] == 'mf' and len(command) == 3:
			print(get_most_frequent(command[1], int(command[2])))
		elif command[0] == 'lf' and len(command) == 3:
			print(get_least_frequent(command[1], int(command[2])))
		elif command[0] == 'pfd' and len(command) == 3:
			plot_freq_dist(command[1], int(command[2]))
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
