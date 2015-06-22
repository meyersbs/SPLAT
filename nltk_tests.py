#################################################################
# File Name: nltk_main.py					#
# Date Created: 06-16-2015					#
# Date Revised: 06-16-2015					#
# Author: Benjamin S. Meyers					#
# Email: bsm9339@rit.edu					#
# 	Advisor: Emily Prud'hommeaux				#
# 	Email: emilypx@rit.edu					#
# 	Advisor: Cissi Ovesdotter-Alm				#
# 	Email: coagla@rit.edu					#
#################################################################
from nltk_functions import *
from nltk_variables import lorem_ipsum_tokens
from nltk_variables import lorem_ipsum_types
from nltk_variables import lorem_ipsum_ttr
from nltk_variables import lorem_ipsum_wc
from nltk_variables import lorem_ipsum_uwc
from nltk_variables import lorem_ipsum_mf30
from nltk_variables import lorem_ipsum_lf30
from nltk_variables import lorem_ipsum_pos
from termcolor import *

pass_count = 0
fail_count = 0

##### TEST FUNCTIONS ############################################
def pause_output():
	get_tokens('moby_dick.txt')
	get_tokens('moby_dick.txt')
	get_tokens('moby_dick.txt')
	get_tokens('moby_dick.txt')
	print('.')
	get_tokens('moby_dick.txt')
	get_tokens('moby_dick.txt')
	get_tokens('moby_dick.txt')
	get_tokens('moby_dick.txt')
	print('.')
	get_tokens('moby_dick.txt')
	get_tokens('moby_dick.txt')
	get_tokens('moby_dick.txt')
	get_tokens('moby_dick.txt')
	print('.')
	get_tokens('moby_dick.txt')
	get_tokens('moby_dick.txt')
	get_tokens('moby_dick.txt')
	get_tokens('moby_dick.txt')

def check_get_tokens():
	global pass_count
	global fail_count
	if get_tokens('lorem_ipsum.txt') == lorem_ipsum_tokens:
		pass_count+=1
		return colored('PASSED!', 'green')
	else:
		fail_count+=1
		return colored('FAILED!', 'red')

def check_get_types():
	global pass_count
	global fail_count
	if get_types('lorem_ipsum.txt') == lorem_ipsum_types:
		pass_count+=1
		return colored('PASSED!', 'green')
	else:
		fail_count+=1
		return colored('FAILED!', 'red')

def check_get_TTR():
	global pass_count
	global fail_count
	if get_TTR('lorem_ipsum.txt') == lorem_ipsum_ttr:
		pass_count+=1
		return colored('PASSED!', 'green')
	else:
		fail_count+=1
		return colored('FAILED!', 'red')

def check_get_word_count():
	global pass_count
	global fail_count
	if get_word_count('lorem_ipsum.txt') == lorem_ipsum_wc:
		pass_count+=1
		return colored('PASSED!', 'green')
	else:
		fail_count+=1
		return colored('FAILED!', 'red')

def check_get_unique_word_count():
	global pass_count
	global fail_count
	if get_unique_word_count('lorem_ipsum.txt') == lorem_ipsum_uwc:
		pass_count+=1
		return colored('PASSED!', 'green')
	else:
		fail_count+=1
		return colored('FAILED!', 'red')

def check_get_most_frequent():
	global pass_count
	global fail_count
	if get_most_frequent('lorem_ipsum.txt', 30) == lorem_ipsum_mf30:
		pass_count+=1
		return colored('PASSED!', 'green')
	else:
		fail_count+=1
		return colored('FAILED!', 'red')

def check_get_least_frequent():
	global pass_count
	global fail_count
	if get_least_frequent('lorem_ipsum.txt', 30) == lorem_ipsum_lf30:
		pass_count+=1
		return colored('PASSED!', 'green')
	else:
		fail_count+=1
		return colored('FAILED!', 'red')

def check_get_pos_counts():
	global pass_count
	global fail_count
	if get_pos_counts('lorem_ipsum.txt') == lorem_ipsum_pos:
		pass_count+=1
		return colored('PASSED!', 'green')
	else:
		fail_count+=1
		return colored('FAILED!', 'red')

def run_tests():
	print('##### RUNNING TESTS #############################################')
	print('\nTesting Token Acquisition')
	pause_output()
	print(check_get_tokens())
	print('\nTesting Type Acquisition')
	pause_output()
	print(check_get_types())
	print('\nTesting Type-Token Ratio Calculation')
	pause_output()
	print(check_get_TTR())
	print('\nTesting Word Count Calculation')
	pause_output()
	print(check_get_word_count())
	print('\nTesting Unique Word Count Calculation')
	pause_output()
	print(check_get_unique_word_count())
	print('\nTesting Most Frequent Word Acquisition')
	pause_output()
	print(check_get_most_frequent())
	print('\nTesting Least Frequent Word Acquisition')
	pause_output()
	print(check_get_least_frequent())
	print('\nTesting Part of Speech Tagging')
	pause_output()
	print(check_get_pos_counts())
	print('\n#################################################################')
	print(colored('Passed: ', 'green') + str(pass_count) + '\t\t' + colored('Failed: ', 'red') + str(fail_count))
	print('#################################################################')
