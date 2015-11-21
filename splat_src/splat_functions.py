#!/usr/bin/python

from __future__ import print_function

########################################################################################################################
##### INFORMATION ######################################################################################################
### @PROJECT_NAME:		SPLAT: Speech Processing and Linguistic Annotation Tool										 ###
### @VERSION_NUMBER:																								 ###
### @PROJECT_SITE:		github.com/meyersbs/SPLAT																     ###
### @AUTHOR_NAME:		Benjamin S. Meyers																			 ###
### @CONTACT_EMAIL:		bsm9339@rit.edu																				 ###
### @LICENSE_TYPE:																									 ###
########################################################################################################################
########################################################################################################################

##### IMPORTS ##########################################################################################################
from nltk.probability import FreqDist
from nltk.tokenize import RegexpTokenizer
from nltk.tree import *
from nltk.util import ngrams
try: from termcolor import *	# The unittest package doesn't like termcolor
except ImportError: pass
from splat_src.splat_global_vars import *
import collections, re, subprocess, sys, nltk
########################################################################################################################

##### HELPER FUNCTIONS #################################################################################################
def determine_output_file(input_file, out_file=None):
	""" Determine whether to write to the original input_file or to a separate out_file. """
	if out_file is None:
		output_file = open(input_file, 'rw')
	else:
		output_file = open(out_file, 'rw')

	return output_file.name
########################################################################################################################

##### ANNOTATION FUNCTIONS #############################################################################################
def insert_speaker_markers(input_file, out_file=None):
	""" Interact with the User to insert speaker indicators into the given text. """
	annotated_file = open('annotated_file.txt', 'w')
	with open(input_file) as f:
		for line in f:
			print('Please enter a speaker marker for: ' + colored(line, 'green'))
			marker = input()
			annotated_file.write(marker + ': ' + line)

	annotated_file.close()
	output_file = determine_output_file(input_file, out_file)
	with open(output_file, 'w') as f1:
		with open(annotated_file.name, 'r') as f2:
			for line in f2:
				f1.write(line)

	os.remove(annotated_file.name)
	return ''

def remove_speaker_markers(input_file, out_file=None):
	""" Remove all speaker indicators from the given text. """
	stripped_file = open('stripped_file.txt', 'w')
	with open(input_file) as f:
		for line in f:
			line = re.sub(r'.:\s', '', line)
			stripped_file.write(line)

	stripped_file.close()
	output_file = determine_output_file(input_file, out_file)
	with open(output_file, 'w') as f1:
		with open(stripped_file.name, 'r') as f2:
			for line in f2:
				f1.write(line)

	os.remove(stripped_file.name)
	return ''

def insert_quarteroni_markers(input_file, out_file=None):
	""" Interact with the User to insert Quarteroni Dialog Acts into the given text. """
	annotated_file = open('annotated_file.txt', 'w')
	with open(input_file) as f:
		for line in f:
			looping = True
			annotation = ' ('
			while looping:
				print ('Please select a dialog act for: ' + colored(line, 'green' + '') + 'Or enter \'0\' to continue...')
				print (q_dialog_acts)
				marker = input()
				if int(marker) == 0:
					annotation = annotation[:-2] + ')\n'
					looping = False
					break
				while marker not in q_numbers or int(marker) not in q_dialog_act_dict.keys():
					marker = input()

				annotation += q_dialog_act_dict[int(marker)] + ', '

			annotated_file.write(line.strip('\n') + annotation)

	annotated_file.close()
	output_file = determine_output_file(input_file, out_file)
	with open(output_file, 'w') as f1:
		with open(annotated_file.name, 'r') as f2:
			for line in f2:
				f1.write(line)

	os.remove(annotated_file.name)
	return ''

def insert_meyers_markers(input_file, out_file=None):
	""" Interact with the User to insert Meyers Dialog Acts into the given text. """
	annotated_file = open('annotated_file.txt', 'w')
	with open(input_file) as f:
		for line in f:
			looping = True
			annotation = ' ('
			while looping:
				print ('Please select a dialog act for: ' + colored(line, 'green' + '') + 'Or enter \'0\' to continue...')
				print (m_dialog_acts)
				marker = input()
				if int(marker) == 0:
					annotation = annotation[:-2] + ')\n'
					looping = False
					break

				while marker not in m_numbers or int(marker) not in m_dialog_act_dict.keys():
					marker = input()

				annotation += m_dialog_act_dict[int(marker)] + ', '

			annotated_file.write(line.strip('\n') + annotation)

	annotated_file.close()
	output_file = determine_output_file(input_file, out_file)
	with open(output_file, 'w') as f1:
		with open(annotated_file.name, 'r') as f2:
			for line in f2:
				f1.write(line)

	os.remove(annotated_file.name)
	return ''

def remove_dialog_acts(input_file, out_file=None):
	""" Remove all Quarteroni & Meyers Dialog Acts from the given text. """
	stripped_file = open('stripped_file.txt', 'w')
	with open(input_file) as f:
		for line in f:
			line = re.sub(r'\(.*\)', '', line)
			stripped_file.write(line.rstrip(' '))

	stripped_file.close()
	output_file = determine_output_file(input_file, out_file)
	with open(output_file, 'w') as f1:
		with open(stripped_file.name, 'r') as f2:
			for line in f2:
				f1.write(line)

	os.remove(stripped_file.name)
	return ''

def insert_utterance_boundaries(input_file, out_file=None):
	""" Automatically parse the input_file and insert basic utterance boundaries. """
	annotated_file = open('annotated_file.txt', 'w')
	new_list = []
	with open(input_file) as f:
		for line in f:
			list_words = str.split(line)
			for word in list_words:
				if (re.search(r'\{SL\}', word) or re.search(r'\{NS\}', word) or re.search(r'\{BR\}', word) or
					re.search(r'\{LS\}', word) or re.search(r'\{LG\}', word) or re.search(r'\{CG\}', word)):
					new_list = new_list
				else:
					new_list.append(word.strip(' \n'))

	curr_line = ''
	found_and, found_so, found_its, found_um, found_could, found_thats = False, False, False, False, False, False
	for new_word in new_list:
		if re.search(r"THAT'S", new_word.upper()):
			found_thats = True
			curr_line += (new_word + ' ')
		elif found_thats and re.search(r'OK', new_word.upper()):
			curr_line = curr_line[:-6]
			annotated_file.write(curr_line)
			curr_line = ('\n' + "THAT'S OK ")
			found_thats = False
		elif re.search(r'OK', new_word) or re.search(r'YEAH', new_word) or re.search(r'ACTUALLY', new_word.upper()):
			annotated_file.write(curr_line)
			curr_line = ('\n' + new_word + ' ')
		elif (re.search(r'MHM', new_word.upper()) or re.search(r'YEP', new_word.upper()) or
			  re.search(r'PERFECT', new_word.upper()) or re.search(r'GOOD', new_word.upper())):
			annotated_file.write(curr_line)
			curr_line = ('\n' + new_word)
			annotated_file.write(curr_line)
			curr_line = '\n'
		elif re.search(r'AND', new_word.upper()):
			found_and = True
			curr_line += (new_word + ' ')
		elif found_and and (re.search(r'THEN', new_word.upper()) or re.search(r'NOW', new_word.upper())):
			curr_line = curr_line[:-4]
			annotated_file.write(curr_line)
			curr_line = ('\n' + 'AND ' + new_word + ' ')
			found_and = False
		elif re.search(r'SO', new_word.upper()):
			found_so = True
			curr_line += (new_word + ' ')
		elif found_so and (re.search(r"I'LL", new_word.upper()) or re.search(r"I'M", new_word.upper()) or re.search(r"^I$", new_word.upper())):
			curr_line = curr_line[:-3]
			annotated_file.write(curr_line)
			curr_line = ('\n' + "SO " + new_word + ' ')
			found_so = False
		elif re.search(r"IT'S", new_word.upper()):
			found_its = True
			curr_line += (new_word + ' ')
		elif found_its and re.search(r'ALRIGHT', new_word.upper()):
			curr_line = curr_line[:-5]
			annotated_file.write(curr_line)
			curr_line = ('\n' + "IT'S ALRIGHT")
			annotated_file.write(curr_line)
			curr_line = '\n'
			found_its = False
		elif re.search(r"UM", new_word.upper()):
			found_um = True
			curr_line += (new_word + ' ')
		elif found_um and re.search(r'NOW', new_word.upper()):
			curr_line = curr_line[:-3]
			annotated_file.write(curr_line)
			curr_line = ('\n' + "UM NOW ")
			found_um = False
		elif re.search(r"COULD", new_word.upper()):
			found_could = True
			curr_line += (new_word + ' ')
		elif found_could and re.search(r'YOU', new_word.upper()):
			curr_line = curr_line[:-6]
			annotated_file.write(curr_line)
			curr_line = ('\n' + "COULD YOU ")
			found_could = False
		else:
			found_and, found_so, found_its, found_um, found_could, found_thats = False, False, False, False, False, False
			curr_line += (new_word + ' ')

	annotated_file.write(curr_line)
	annotated_file.close()
	output_file = determine_output_file(input_file, out_file)
	with open(output_file, 'w') as f1:
		with open(annotated_file.name, 'r') as f2:
			for line in f2:
				f1.write(line)

	os.remove(annotated_file.name)
	return ''

def remove_utterance_boundaries(input_file, out_file=None):
	""" Remove all utterance boundaries from the input_file. """
	if out_file is None:
		stripped_file = open('stripped_file.txt', 'w')
	else:
		stripped_file = open(out_file, 'w')

	with open(input_file, 'r') as f:
		for line in f:
			stripped_file.write(line[:-1])

	stripped_file.close()
	output_file = determine_output_file(input_file, out_file)
	with open(output_file, 'w') as f1:
		with open(stripped_file.name, 'r') as f2:
			for line in f2:
				f1.write(line)

	os.remove(stripped_file.name)
	return ''
########################################################################################################################

##### ANNOTATION METRICS ###############################################################################################
def count_meyers_markers(input_file):
	""" Count the frequency for each Meyers Dialog Act. """
	pre_markers = ''
	m_stats = {'Info-Request':		[0,0,0], 'Action-Request':	[0,0,0], 'Action-Suggest':			[0,0,0],
			   'Answer-Yes':		[0,0,0], 'Answer-No':		[0,0,0], 'Answer-Neutral':			[0,0,0],
			   'Apology':			[0,0,0], 'Thanks':			[0,0,0], 'Clarification-Request':	[0,0,0],
			   'Acknowledgment':	[0,0,0], 'Filler':			[0,0,0], 'Inform':					[0,0,0],
			   'Other':				[0,0,0], 'Multiple':		[0,0,0]}
	with open(input_file) as f:
		for line in f:
			split_line = line.split('(')
			if len(split_line) >= 2:
				pre_markers = split_line[1].strip(')\n')
			else:
				pass

			if pre_markers.__contains__(','):
				m_stats['Multiple'][0] += 1
				for item in pre_markers.split(', '):
					m_stats[item][0]+=1
					new_line = re.sub(r'\(.*\)', '', re.sub(r'\{SL\}', '', re.sub(r'^.:\s', '', item)))
					m_stats[item][1] += len(new_line.split())
			elif pre_markers in m_dialog_act_dict.values():
				m_stats[pre_markers][0] += 1
				new_line = re.sub(r'\(.*\)', '', re.sub(r'\{SL\}', '', re.sub(r'^.:\s', '', line)))
				m_stats[pre_markers][1] += len(new_line.split())

	return m_stats

def get_meyers_metrics(input_file):
	""" Displays the analysis of Meyers Dialog Acts to stdout. """
	m_stats = count_meyers_markers(input_file)
	output = ''
	for item in sorted(m_stats.keys()):
		if m_stats[item][0] != 0:
			#output += colored(item, 'green') + ' Count: ' + str(m_stats[item][0]) + '\n'
			output += 'Average Words per Utterance with ' + colored(item, 'green') + ' marker: ' + str(float(m_stats[item][1])/m_stats[item][0]) + '\n'
			#percent_total += float(m_stats[item][0])/float(get_num_utterances(input_file))*float(100)
			output += (str(float(m_stats[item][0])/float(get_num_utterances(input_file))*float(100)) + '% of utterances are ' + colored(item, 'green') + '\n')
			#output += str(float(m_stats[item][0])/float(get_num_utterances(input_file))*float(100)) + '\n'
		else:
			output += colored(item, 'green') + ' Count: ' + str(0) + '\n'
			output += 'Average Words per Utterance with ' + colored(item, 'green') + ' marker: ' + str(0.00) + '\n'
			#output += (str(0.00) + '% of utterances are ' + colored(item, 'green') + '\n')
			#output += str(0) + '\n'

	return output

def get_wc_ds_per_act(input_file): #Dis Count, Act Count
	""" List word count and disfluency count per utterance for each dialog act. """
	pre_markers = ''
	dialog_dis = {'Acknowledgment': [0,0,[]], 'Action-Request':			[0,0,[]], 'Action-Suggest': 	[0,0,[]],
				  'Answer-Neutral': [0,0,[]], 'Answer-No':				[0,0,[]], 'Answer-Yes':			[0,0,[]],
				  'Apology':		[0,0,[]], 'Clarification-Request': 	[0,0,[]], 'Filler':				[0,0,[]],
				  'Info-Request':	[0,0,[]], 'Inform':					[0,0,[]], 'Other':				[0,0,[]],
				  'Thanks':			[0,0,[]]}
	with open(input_file) as f:
		for line in f:
			split_line = line.split('(')
			if len(split_line) >= 2:
				pre_markers = split_line[1].strip(')\n')
			else:
				pass

			if pre_markers.__contains__(','):
				for item in pre_markers.split(', '):
					dialog_dis[item][1]+=1
					dialog_dis[item][2].append(re.sub(r'.*:\s', '', split_line[0]))
					for word in re.sub(r'.*:\s', '', split_line[0]).split():
						if word.lower() in disfluency_list or word == '{SL}':
							dialog_dis[item][0] += 1
			elif pre_markers in m_dialog_act_dict.values():
				for item in pre_markers.split():
					dialog_dis[item][1]+=1
					dialog_dis[item][2].append(re.sub(r'.*:\s', '', split_line[0]))
					for word in re.sub(r'.*:\s', '', split_line[0]).split():
						if word.lower() in disfluency_list or word == '{SL}':
							dialog_dis[item][0] += 1

	for key in sorted(dialog_dis.keys()):
		print(key)
		print('Word Count\tDisfluency Count')
		for line in dialog_dis[key][2]:
			#print(str(len(line)))
			count = 0
			for word in line.split():
				if word.lower() in disfluency_list or word == '{SL}':
					count+=1

			print(str(len(line)) + '\t\t' + str(count))
		try:
			print('')
			#print(float(dialog_dis[key][0]) / float(dialog_dis[key][1]))
		except ZeroDivisionError:
			pass

	return ''
########################################################################################################################

##### NORMALIZATION FUNCTIONS ##########################################################################################
def __normalize_word(word):
	""" Normalize a single word by removing punctuation. Ignores annotation. """
	if word[0] == '(' or word[-1] == ')' or word[-1] == ',' or word[-1] == '-' or word[0] == '-':
		return ''
	tokenizer = RegexpTokenizer(r"^[a-zA-Z\'\-]{1,}$") # Remove all non-word-characters from the given word.
	new_word = tokenizer.tokenize(word.strip('.').strip(',').lower())

	try:
		return new_word[0]
	except IndexError:
		return '-1'

def normalize_text(input_file):
	""" Normalizes every word in the given input_file. """
	normal_text = '\n'
	with open(input_file) as curr_file:
		for line in curr_file:
			normal_line = ''
			for word in line.split():
				if word != '{SL}' and word != 'S:':
					normal_line += __normalize_word(word) + ' '

			normal_text += normal_line + '\n'

	return normal_text

def strip_annotation(input_file):
	""" Remove all forms of annotation from the given input_file. """
	stripped_file = open('/usr/bin/splat_tmp/stripped_file.txt', 'w')
	with open(input_file) as f:
		for line in f:
			new_line_1 = re.sub(r'\{SL\}\s', '', re.sub(r'\s\w*\-\s', ' ', re.sub(r'\s\(.*\)', '', re.sub(r'.:\s', '', line))))
			new_line_2 = new_line_1.replace('.', '').replace(',', '').replace('!', '').replace('?', '').replace(' \n', '\n')
			stripped_file.write(new_line_2)

	stripped_file.close()

	return stripped_file.name
########################################################################################################################

##### UTTERANCE-BASED FEATURES #########################################################################################
def get_utterances(input_file):
	""" Save each utterance from the given input_file into a list, stripping annotation. """
	utterances = []
	new_line = ''
	with open(input_file) as curr_file:
		for line in curr_file:
			if line[0] == '(':
				new_line = line[15:]
				utterances.append(new_line.strip('\n'))
			elif (line[0] == 'F' or line[0] == 'S' or line[0] == 'T') and line[1] == ':':
				new_line = line[3:]
				utterances.append(new_line.strip('\n'))
			elif line[0] == '\t' or line[0] == '\n':
				new_line = new_line
			else:
				new_line = line
				utterances.append(new_line.strip('\n'))

	return utterances

def get_num_utterances(input_file):
	""" Return the total number of utterances in the given input_file. """
	return len(get_utterances(input_file))

def list_utterances(input_file):
	""" Display all of the utterances from the given input_file. """
	for item in get_utterances(input_file): print(item + '\n')
	return ''

def get_avg_utterance_length(input_file):
	""" Calculate the average utterance length. """
	return round((float(get_word_count(input_file)) / get_num_utterances(input_file)), 4)
########################################################################################################################

##### FREQUENCY-BASED FEATURES #########################################################################################
def get_freq_dist(input_file):
	""" Calculate the frequency distribution for the given input_file. """
	new_words = []
	for token in get_tokens(input_file):
		if re.match(r'^F', token) or re.match(r'^S', token) or re.match(r'^T', token) or re.match(r'\{SL\}', token):
			new_words = new_words
		else:
			new_words.append(token)

	return FreqDist(new_words)

def plot_freq_dist(input_file, x = None):
	""" Plot the frequency distribution for the given input_file. """
	if x is None:
		get_freq_dist(input_file).plot()
	else:
		get_freq_dist(input_file).plot(int(x))

	return ''

def get_most_frequent(input_file, x = None):
	""" Get the top x most frequent tokens. """
	if x is None:
		return get_freq_dist(input_file).most_common()
	else:
		return get_freq_dist(input_file).most_common(int(x))

def get_least_frequent(input_file, x = None):
	""" Get the x least frequent tokens. """
	most_common = get_most_frequent(input_file, get_word_count(input_file))
	freq_dist = []
	count = 0

	if x is None:
		freq_dist = most_common
	else:
		for item in reversed(most_common):
			if count < int(x):
				freq_dist.append(item)
				count += 1

	return freq_dist
########################################################################################################################

##### TYPE-TOKEN-BASED FEATURES ########################################################################################
def get_tokens(input_file):
	""" Generate a list of tokens. """
	global pause_count, break_count, total_disfluencies
	pause_count, break_count, total_disfluencies = 0, 0, 0
	raw_file = open(input_file)
	raw_text = raw_file.read()
	normalized_raw = ''

	stripped_raw = re.sub(r'[.,!?]', '',  re.sub(r'\s\(.*\)', '', raw_text))

	for item in stripped_raw.split():
		normal_item = '-1'
		if re.match(r'^.:$', item):
			pass
		elif item == '{SL}':
			pause_count += 1
		elif re.match(r'^.*-$', item):
			break_count += 1
			#normal_item = __normalize_word(item)
		else:
			normal_item = __normalize_word(item)

		if normal_item != '-1':
			normalized_raw += normal_item + '\n'

	tokens = RegexpTokenizer(r'[^\d\s\:\(\)]+').tokenize(normalized_raw)

	raw_file.close()
	return tokens

def get_types(input_file):
	""" Generate a list of types. """
	return set(get_tokens(input_file))

def get_word_count(input_file):
	""" Count the number of tokens. """
	return len(get_tokens(input_file))

def get_unique_word_count(input_file):
	""" Count the number of types. """
	return len(get_types(input_file))

def get_ttr(input_file):
	""" Calculate the Type-Token Ratio. """
	return round((float(get_unique_word_count(input_file)) / get_word_count(input_file) * 100), 4)

def get_words_per_utterance(input_file):
	""" Return a word count for each individual utterance in CSV format. """
	utterances = get_utterances(input_file)
	output = ''
	for line in utterances:
		wordcount = len(line.split())
		output += ('\n' + str(wordcount))

	return output
########################################################################################################################

##### SYNTAX-BASED FEATURES ############################################################################################
def tag_pos(input_file):
	""" Tag all types with parts of speech. """
	return nltk.pos_tag(get_tokens(input_file))

def get_pos_counts(input_file):
	""" Calculate the total number of types for each part of speech tag. """
	pos_counts = {}
	for (k, v) in dict(tag_pos(input_file)).items():
		if v in pos_counts.keys():
			pos_counts[v] += 1
		else:
			pos_counts.update({v: 1})

	return pos_counts

def calc_content_density(input_file):
	""" Calculate the content density. """
	open_class_count, closed_class_count = 0, 0

	for (k, v) in dict(tag_pos(input_file)).items():
		if v in open_class_list:
			open_class_count += 1
		elif v not in ignore_list:
			closed_class_count += 1

	return float(open_class_count) / closed_class_count

def calc_idea_density(input_file):
	""" Calculate the idea density. """
	proposition_count = 0
	for (k, v) in dict(tag_pos(input_file)).items():
		if v in proposition_list:
			proposition_count += 1

	return float(proposition_count) / get_word_count(input_file)

def get_content_words(input_file):
	""" Get a list of all content words. """
	content_words = []
	for word in get_tokens(input_file):
		if word.lower() not in stopwords:
			content_words.append(word)

	return content_words

def get_unique_content_words(input_file):
	""" Get a list of unique content words. """
	content_words = []
	for word in get_types(input_file):
		if word.lower() not in stopwords:
			content_words.append(word)

	return content_words

def get_function_words(input_file):
	""" Get a list of all function words. """
	function_words = []
	for word in get_tokens(input_file):
		if word.lower() in stopwords:
			function_words.append(word)

	return function_words

def get_unique_function_words(input_file):
	""" Get a list of unique function words. """
	function_words = []
	for word in get_types(input_file):
		if word.lower() in stopwords:
			function_words.append(word)

	return function_words

def get_content_function_ratio(input_file):
	""" Calculate the content-function word ratio. """
	content = get_content_words(input_file)
	function = get_function_words(input_file)

	#print(len(content))
	#print(len(function))
	ratio = float(len(content)) / float(len(function))

	return round(ratio, 4)
########################################################################################################################

##### LANGUAGE MODEL FEATURES ##########################################################################################
def get_unigrams(input_file):
	""" Get all unigrams. """
	utterances = get_utterances(input_file)
	text = []
	for utterance in utterances:
		for word in utterance.split():
			text.append(re.sub(r'[\.,!\?:;]', "", word.lower()))
	print(text)
	return ngrams(text, 1)

def get_bigrams(input_file):
	""" Get all bigrams. """
	utterances = get_utterances(input_file)
	text = []
	for utterance in utterances:
		for word in utterance.split():
			text.append(re.sub(r'[\.,!\?:;]', "", word.lower()))
	print(text)
	return ngrams(text, 2)

def get_trigrams(input_file):
	""" Get all trigrams. """
	utterances = get_utterances(input_file)
	text = []
	for utterance in utterances:
		for word in utterance.split():
			text.append(re.sub(r'[\.,!\?:;]', "", word.lower()))
	print(text)
	return ngrams(text, 3)

def get_ngrams(input_file, n=2):
	""" Get all ngrams of a given size. Defaults to bigrams. """
	try:
		n = int(n)
	except ValueError:
		n=2
	utterances = get_utterances(input_file)
	text = []
	for utterance in utterances:
		for word in utterance.split():
			text.append(re.sub(r'[\.,!\?:;]', "", word.lower()))
	print(text)
	return ngrams(text, n)

########################################################################################################################

##### BERKELEY PARSER FEATURES #########################################################################################
def get_parse_trees(input_file):
	""" Use the Berkeley Parser to obtain parse-tree-strings for each line in the input_file. """
	clean_file = strip_annotation(input_file)
	parse_trees = []
	parse_trees.append(subprocess.check_output(['java', '-jar', 'BerkeleyParser-1.7.jar', '-gr', 'eng_sm6.gr',
												'-inputFile', clean_file], cwd = '/usr/bin/splat_src',
											    shell = False).strip('\n'))
	os.remove(clean_file)
	return parse_trees

def get_formatted_trees(input_file):
	""" Format the parse-tree-strings so they can be fed to the Frazier & Yngve parsers. """
	raw_trees = get_parse_trees(input_file)
	form_trees = []
	for item in raw_trees[0].split('\n'):
		form_trees.append('( ' + item + ' )\n')

	return form_trees

def print_formatted_trees(input_file):
	""" Print the formatted parse-tree-strings from input_file. """
	output = ''
	for tree_string in get_formatted_trees(input_file):
		output += tree_string

	return output

def draw_trees(input_file):
	""" Draws pictures of each parse-tree-string using Matplotlib. """
	form_trees = get_formatted_trees(input_file)
	for tree_string in form_trees:
		print(tree_string)
		sentence = Tree.parse(tree_string)
		sentence.draw()

	return ''

def get_max_depths(input_file):
	""" Calculate the max depths for each parse tree. """
	count = 0
	depths = {}
	lines = []
	with open(input_file) as f:
		for line in f:
			lines.append(line.strip('\n').strip('.').strip(','))

	for item in get_parse_trees(input_file):
		curr_depth, max_depth = 0, 0
		for sentence in item.split('\n'):
			for word in sentence.split():
				for char in word:
					if char == '(':
						curr_depth += 1
					elif char == ')':
						curr_depth -= 1
					else:
						curr_depth = curr_depth

					if curr_depth > max_depth:
						max_depth = curr_depth

			depths[lines[count]] = max_depth
			count += 1

	max_depth = 0
	for val in depths.values():
		if val > max_depth:
			max_depth = val

	return max_depth

def print_max_depths(input_file):
	"""  Display the max depths for each parse tree from the input_file. """
	output = 'max depth,sentence'
	depths = get_max_depths(input_file)
	for key in depths.keys():
		output += ('\n' + str(depths[key]) + ',' + key)

	return output
########################################################################################################################

##### YNGVE & FRAZIER SCORING ##########################################################################################
# The code contained in this section was adapted based on the code located here:
# https://github.com/neubig/util-scripts/blob/96c91e43b650136bb88bbb087edb1d31b65d389f/syntactic-complexity.py
# Permission was granted by Graham Neubig, the code creator, to use his code. For questions regarding his code,
# he may be contacted by email < neubig@is.naist.jp > or you can visit his website
# http://www.phontron.com/index.php
def get_word_score(tree):
	""" Calculate the word score for each tree. """
	if type(tree) == str:
		return 1
	else:
		score = 0
		for child in tree:
			score += get_word_score(child)
		return score

def is_sentence(value):
	""" Determine if the given string is a sentence. """
	if len(value) > 0 and value[0] == "S":
		return True
	else:
		return False

def calc_yngve_score(tree, parent):
	""" Calculate the Yngve Score for a given input_file. """
	if type(tree) == str:
		return parent
	else:
		count = 0
		for i, child in enumerate(reversed(tree)):
			count += calc_yngve_score(child, parent + i)
		return count

def calc_frazier_score(tree, parent, parent_label):
	""" Calculate the Frazier Score for a given input_file. """
	my_lab = ''
	if type(tree) == str:
		return parent - 1
	else:
		count = 0
		for i, child in enumerate(tree):
			score = 0
			if i == 0:
				my_lab = tree.node
				if is_sentence(my_lab):
					score = (0 if is_sentence(parent_label) else parent + 1.5)
				elif my_lab != "" and my_lab != "ROOT" and my_lab != "TOP":
					score = parent + 1
			count += calc_frazier_score(child, score, my_lab)
		return count

def get_yngve_score(input_file):
	""" Average all of the yngve scores for the given input_file. """
	sentences, total_yngve_score = 0, 0
	for tree_line in get_formatted_trees(input_file):
		#print(tree_line)
		if tree_line.strip() == "":
			continue
		tree = Tree.parse(tree_line)
		sentences += 1
		raw_yngve_score = calc_yngve_score(tree, 0)
		try:
			mean_yngve_score = float(raw_yngve_score) / float(get_word_score(tree))
			total_yngve_score += mean_yngve_score
		except ZeroDivisionError:
			print('WARNING: ZeroDivisionError for the tree: ' + str(tree), file=sys.stderr)
			pass

	return float(total_yngve_score) / sentences

def get_frazier_score(input_file):
	""" Average all of the frazier scores for the given input_file. """
	sentences, total_frazier_score = 0, 0
	for tree_line in get_formatted_trees(input_file):
		if tree_line.strip() == "":
			continue
		tree = Tree.parse(tree_line)
		sentences += 1
		raw_frazier_score = calc_frazier_score(tree, 0, "")
		try:
			mean_frazier_score = float(raw_frazier_score) / float(get_word_score(tree))
			total_frazier_score += mean_frazier_score
		except ZeroDivisionError:
			print('WARNING: ZeroDisvisionError for the tree: ' + str(tree), file=sys.stderr)
			pass

	return float(total_frazier_score) / sentences

def new_yngve(treestring):
	just_pushed = False
	stack = 0
	total = 0
	for char in treestring:
		if char == "(":
			just_pushed = True
			stack += 1
		elif char == ")":
			if just_pushed:
				total += stack
			just_pushed = False
			stack -= 1

	return total

def yngve(treestrings):
	individual_scores = 0
	for treestring in treestrings:
		individual_scores += new_yngve(treestring)

	return float(individual_scores) / float(len(treestrings))
########################################################################################################################
########################################################################################################################

########################################################################################################################
##### DISFLUENCY-BASED FEATURES ########################################################################################
def count_disfluencies(input_file):
	""" Count the number of various disfluencies in a given input_file. """
	global pause_count, break_count, total_disfluencies
	um_count, uh_count, ah_count, er_count, hm_count, rep_count = 0, 0, 0, 0, 0, 0
	last_item = ''
	for item in get_tokens(input_file):
		if item == 'um':
			um_count += 1
		elif item == 'uh':
			uh_count += 1
		elif item == 'ah':
			ah_count += 1
		elif item == 'er':
			er_count += 1
		elif item == 'hm':
			hm_count += 1

		if last_item == item:
			rep_count += 1
		if item != '{SL}':
			last_item = item

	nasal_filled = hm_count + um_count
	non_nasal_filled = uh_count + ah_count + er_count
	total_disfluencies = break_count + pause_count + nasal_filled + non_nasal_filled + rep_count

	output = ('UM Count: ' + str(um_count))
	output += ('\nHM Count: ' + str(hm_count))
	output += ('\nNasal-Filled Disfluency Count: ' + str(nasal_filled))
	output += ('\nUH Count: ' + str(uh_count))
	output += ('\nER Count: ' + str(er_count))
	output += ('\nAH Count: ' + str(ah_count))
	output += ('\nNon-Nasal-Filled Disfluency Count: ' + str(non_nasal_filled))
	output += ('\nSilent Pause Count: ' + str(pause_count))
	output += ('\nBreak Count: ' + str(break_count))
	output += ('\nRepetition Count: ' + str(rep_count))
	output += ('\nTotal Disfluency Count: ' + str(total_disfluencies))

	return output

def get_disfluencies_per_utterance(input_file):
	""" Return a disfluency count for each individual utterance in CSV format. """
	count = 1
	output, last_item = '', ''
	for line in get_utterances(input_file):
		dis_count, nasal_count, non_nasal_count, other_count, word_count, um_count, uh_count = 0, 0, 0, 0, 0, 0, 0
		for item in line.split():
			word_count += 1
			if item == '{SL}':
				dis_count += 1
				other_count += 1
			elif __normalize_word(item) in nasal_list:
				nasal_count += 1
				#dis_count += 1
				if __normalize_word(item) != 'um' or __normalize_word(item) != 'uh':
					dis_count += 1
				if __normalize_word(item) == 'um':
					um_count += 1
				if __normalize_word(item) == 'uh':
					uh_count += 1
			elif __normalize_word(item) in non_nasal_list:
				non_nasal_count += 1
				if __normalize_word(item) != 'um' or __normalize_word(item) != 'uh':
					dis_count += 1
				if __normalize_word(item) == 'um':
					um_count += 1
				if __normalize_word(item) == 'uh':
					uh_count += 1
			elif re.match(r'^.*-$', item):
				other_count += 1
				dis_count += 1

			if last_item == item:
				dis_count = dis_count
				#dis_count += 1
				other_count += 1

			if item != '{SL}':
				last_item = item

		output += ('\n' + str(float(uh_count))) #+ ',' + str(float(non_nasal_count)/word_count))
		count += 1

	return output
########################################################################################################################

##### JUST PRINTING FUNCTIONS ##########################################################################################
def display_command_list():
	""" Print a list of commands to stdout. """
	print ('command\t\targ1\t\targ2\tdescription\t\t\t\t')
	for item in collections.OrderedDict(sorted(command_info.items())):
		print (colored(item, 'green') + colored(command_args[item], 'blue') + colored('\t' + command_info[item], 'yellow'))
	print('\n\t\t\t\t' + colored('*', 'red') + colored('\tDenotes an Optional Argument', 'yellow'))
	return ''

def print_usage_instructions():
	""" Print basic usage instructions to stdout. """
	usage = '\nInvalid command. For a list of available commands, use ' + colored('--commands', 'green') + '.'
	usage += '\nCommands look like this: ' + colored('splat', 'red') + ' ' + colored('COMMAND', 'green') + ' ' + colored('*', 'red') + colored('arg1', 'blue') + ' ' + colored('*', 'red') + colored('arg2', 'blue') + ' ' + colored('filename', 'yellow')
	usage += '\n' + colored('*', 'red') + ' denotes an optional argument.'
	usage += '\n\n' + colored('Warning:', 'red') + ' Large inputs, such as Moby Dick, will take longer to process.'

	print(usage)
	return ''

def info(opt = None):
	""" Print basic program info to stdout. """
	prog_info = '#################################################################'
	prog_info += '\n# SPLAT - Speech Processing & Linguistic Annotation Tool \t#'
	prog_info += '\n# Release 3.00 \tAugust 4, 2015 \t\t\t\t\t#'
	prog_info += '\n# Developed by Benjamin S. Meyers\t\t\t\t#'
	prog_info += '\n#\t\t\t\t\t\t\t\t#'
	prog_info += '\n# This application may not be copied, altered, or distributed \t#'
	prog_info += '\n# without written consent from the product owner. \t\t#'
	prog_info += '\n# \t\t\t\t\t\t\t\t#'
	prog_info += '\n# For documentation, visit: https://github.com/meyersbs/SPLAT \t#'
	prog_info += '\n# \t\t\t\t\t\t\t\t#'
	prog_info += '\n#################################################################'

	if opt is None:
		print(prog_info)
	elif opt == '42':
		print("DON'T PANIC!")
	else:
		print_usage_instructions()

	return ''

def version_info():
	""" Print most recent version of CLAAP. """
	return versions[0]

def print_help(command=None):
	""" Print help info. """
	output = '\n' + colored('command', 'green') + colored('\t\targ1\t\targ2', 'blue') + colored('\tdescription', 'yellow')
	if command is None:
		output += '\n' + colored('--commands', 'green') + colored('\t\t\t\t' + command_info['--commands'], 'yellow')
		output += '\n' + colored('--info', 'green') + colored('\t\t\t\t\t' + command_info['--info'], 'yellow')
		output += '\n' + colored('--usage', 'green') + colored('\t\t\t\t\t' + command_info['--usage'], 'yellow')
		output += '\n' + colored('--version', 'green') + colored('\t\t\t\t' + command_info['--version'], 'yellow')
	elif command in command_info.keys():
		output += '\n' + colored(command, 'green') + colored(command_args[command], 'blue') + colored('\t' + command_info[command], 'yellow')
	return output
########################################################################################################################
