#!/usr/bin/python

##### IMPORTS ##########################################################################################################
from nltk.probability import FreqDist
from nltk.tokenize import RegexpTokenizer
from nltk.tree import *
from termcolor import *
from claap_global_vars import *
import collections
import nltk
import re
import subprocess
########################################################################################################################


##### NORMALIZATION FUNCTIONS ##########################################################################################
# Take the given word, convert to lowercase and strip punctuation.
def __normalize_word(word):
    # Remove all non-word-characters from the given word.
    tokenizer = RegexpTokenizer(r'^[\w\']*')
    new_word = tokenizer.tokenize(word.strip('.').strip(',').lower())

    try:
        return new_word[0]
    except IndexError:
        return '-1'


# Take the given text file and return it after normalization of each word.
def normalize_text(text_file):
    normal_text = '\n'
    with open(text_file) as curr_file:
        for line in curr_file:
            normal_line = ''
            for word in line.split():
                if word != '{SL}' and word != 'S:':
                    normal_line += __normalize_word(word) + ' '
            normal_text += normal_line + '\n'
    return normal_text
########################################################################################################################


##### UTTERANCE-BASED FEATURES #########################################################################################
# Save each utterance (line) into an array, stripping annotation.
def get_utterances(text_file):
    utterances = []
    with open(text_file) as curr_file:
        for line in curr_file:
            if line[0] == '(':
                new_line = line[15:]
                utterances.append(new_line.strip('\n'))
            elif line[0] == 'F' or line[0] == 'S' or line[0] == 'T':
                new_line = line[3:]
                utterances.append(new_line.strip('\n'))
            elif line[0] == '\t' or line[0] == '\n':
                new_line = new_line
            else:
                new_line = line
                utterances.append(new_line.strip('\n'))

    return utterances


# Return the total number of utterances.
def get_num_utterances(text_file):
    utterances = get_utterances(text_file)
    count = len(utterances)

    return count


# Display a list of utterances.
def list_utterances(text_file):
    utterances = get_utterances(text_file)
    for item in utterances:
        print(item + '\n')

    return ''


# Calculate the average utterance length.
def get_avg_utterance_length(text_file):
    num_words = get_word_count(text_file)
    count = get_num_utterances(text_file)

    avg = float(num_words) / count
    return round(avg, 4)
########################################################################################################################


##### FREQUENCY-BASED FEATURES #########################################################################################
# Calculate the frequency distribution.
def get_freq_dist(text_file):
    all_words = get_tokens(text_file)
    new_words = []
    for token in all_words:
        if re.match(r'^F', token):      new_words = new_words
        elif re.match(r'^S', token):    new_words = new_words
        elif re.match(r'^T', token):    new_words = new_words
        elif re.match(r'{SL}', token):  new_words = new_words
        else:                           new_words.append(token)

    freq_dist = FreqDist(new_words)

    return freq_dist


# Plot the frequency distribution.
def plot_freq_dist(text_file, x = None):
    freq_dist = get_freq_dist(text_file)

    if x is None:   freq_dist.plot()
    else:           freq_dist.plot(int(x))

    return ''


# Display the top x most frequent tokens.
def get_most_frequent(text_file, x = None):
    freq_dist = get_freq_dist(text_file)

    if x is None:   return freq_dist.most_common()
    else:           return freq_dist.most_common(int(x))


# Display the top x least frequent tokens.
def get_least_frequent(text_file, x = None):
    most_common = get_most_frequent(text_file, get_word_count(text_file))

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
# Generate a list of tokens.
def get_tokens(text_file):
    global pause_count
    global break_count
    pause_count = 0
    break_count = 0
    global total_disfluencies
    total_disfluencies = 0
    curr_file = open(text_file)
    raw = curr_file.read()

    normalized_raw = ''
    for item in raw.split():
        normal_item = '-1'
        if re.match(r'^.:$', item):
            pass
        elif item == '{SL}':
            pause_count += 1
        elif re.match(r'^.*-$', item):
            break_count += 1
            normal_item = __normalize_word(item)
        else:
            normal_item = __normalize_word(item)

        if normal_item != '-1':
            normalized_raw += normal_item + '\n'

    tokens = RegexpTokenizer(r'[^\d\s\:\(\)]+').tokenize(normalized_raw)

    return tokens


# Generate a list of types.
def get_types(text_file):
    tokens = get_tokens(text_file)
    types = set(tokens)

    return types


# Generate a Total Word Count.
def get_word_count(text_file):
    tokens = get_tokens(text_file)
    word_count = len(tokens)

    return word_count


# Generate a Unique Word Count.
def get_unique_word_count(text_file):
    types = get_types(text_file)
    unique_word_count = len(types)

    return unique_word_count


# Calculate the Type-Token Ratio.
def get_ttr(text_file):
    num_types = get_unique_word_count(text_file)
    num_tokens = get_word_count(text_file)
    type_token_ratio = float(num_types) / num_tokens * 100

    return round(type_token_ratio, 4)


# Return a word count for each individual utterance in csv format.
def get_words_per_utterance(text_file):
    utterances = get_utterances(text_file)
    count = 1
    output = ''
    for line in utterances:
        wordcount = len(line.split())
        output += ('\n' + str(count) + ',' + str(wordcount))
        count += 1

    return output
########################################################################################################################


##### SYNTAX-BASED FEATURES ############################################################################################
# Tag all Types with Parts of Speech.
def tag_pos(text_file):
    tokens = get_tokens(text_file)
    parts_of_speech = nltk.pos_tag(tokens)

    return parts_of_speech


# Calculate the Total Number for each POS.
def get_pos_counts(text_file):
    pos = dict(tag_pos(text_file))

    pos_counts = {}
    for (k, v) in pos.items():
        if v in pos_counts.keys():  pos_counts[v] += 1
        else:                       pos_counts.update({v: 1})

    return pos_counts


# Calculate the Content Density of a given text_file.
def calc_content_density(text_file):
    pos = dict(tag_pos(text_file))
    open_class_count = 0
    closed_class_count = 0

    for (k, v) in pos.items():
        if v in open_class_list:
            open_class_count += 1
        elif v not in ignore_list:
            closed_class_count += 1
        else:
            open_class_count = open_class_count
            closed_class_count = closed_class_count

    return float(open_class_count) / closed_class_count


# Calculate the Idea Density of a given text_file.
def calc_idea_density(text_file):
    pos = dict(tag_pos(text_file))
    word_count = get_word_count(text_file)
    proposition_count = 0
    proposition_list
    for (k, v) in pos.items():
        if v in proposition_list: proposition_count += 1

    return float(proposition_count) / word_count


# List all of the content words within the given text file.
def get_content_words(text_file):
    tokens = get_tokens(text_file)
    content_words = []
    for word in tokens:
        if word.lower() not in stopwords: content_words.append(word)

    return content_words


# List all of the unique content words within the given text file.
def get_unique_content_words(text_file):
    types = get_types(text_file)
    content_words = []
    for word in types:
        if word.lower() not in stopwords: content_words.append(word)

    return content_words


# List all of the function words within the given text file.
def get_function_words(text_file):
    tokens = get_tokens(text_file)
    function_words = []
    for word in tokens:
        if word.lower() in stopwords: function_words.append(word)

    return function_words


# List all of the unique function words within the given text file.
def get_unique_function_words(text_file):
    types = get_types(text_file)
    function_words = []
    for word in types:
        if word.lower() in stopwords: function_words.append(word)

    return function_words


# Calculate the ratio of content words to function words.
def get_content_function_ratio(text_file):
    content = get_content_words(text_file)
    function = get_function_words(text_file)

    print(len(content))
    print(len(function))
    ratio = float(len(content)) / float(len(function))

    return round(ratio, 4)
########################################################################################################################


##### BERKELEY PARSER FEATURES #########################################################################################
# Use the Berkeley Parser to obtain parse trees for each sentence in a text file.
def get_parse_trees(text_file):
    parse_trees = []
    parse_trees.append(subprocess.check_output(['java', '-jar', 'BerkeleyParser-1.7.jar', '-gr', 'eng_sm6.gr',
                                                '-inputFile', str(text_file)], shell = False).strip('\n'))

    return parse_trees


# Format parse trees for Frazier & Yngve Scoring.
def get_formatted_trees(text_file):
    raw_trees = get_parse_trees(text_file)
    form_trees = []
    for item in raw_trees[0].split('\n'):
        form_trees.append('( ' + item + ' )\n')
    return form_trees


# Prints the formatted tree strings.
def print_formatted_trees(text_file):
    form_trees = get_formatted_trees(text_file)
    output = ''
    for tree_string in form_trees:
        output += tree_string

    return output


# Takes a text_file, parses and formats into trees, and draws the trees.
def draw_trees(text_file):
    form_trees = get_formatted_trees(text_file)
    for tree_string in form_trees:
        sentence = Tree.fromstring(tree_string)
        sentence.draw()

    return ''


# Takes in a properly formatted Berkeley Parse Tree and calculates max depth.
def get_max_depths(text_file):
    count = 0
    curr_depth = 0
    max_depth = 0
    depths = {}
    lines = []
    with open(text_file) as f:
        for line in f:
            lines.append(line.strip('\n').strip('.').strip(','))

    trees = get_parse_trees(text_file)
    for item in trees:
        curr_depth = 0
        max_depth = 0
        for sentence in item.split('\n'):
            for word in sentence.split():
                for char in word:
                    if char == '(':     curr_depth += 1
                    elif char == ')':   curr_depth -= 1
                    else:               curr_depth = curr_depth

                    if curr_depth > max_depth: max_depth = curr_depth

            depths[lines[count]] = max_depth
            count += 1

    return depths


# Prints the max depths of the parse tree for each sentence in the given text_file
def print_max_depths(text_file):
    output = 'max depth,sentence'
    depths = get_max_depths(text_file)
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

# Calculate word score.
def get_word_score(tree):
    if type(tree) == str: return 1
    else:
        count = 0
        for child in tree: count += get_word_score(child)
        return count


# Determine if it is a sentence.
def is_sentence(value):
    if len(value) > 0 and value[0] == "S":  return True
    else:                                   return False


# Calculate the Yngve Score for a given text_file.
def calc_yngve_score(tree, parent):
    if type(tree) == str: return parent
    else:
        count = 0
        for i, child in enumerate(reversed(tree)): count += calc_yngve_score(child, parent+i)
        return count


# Calculate the Frazier Score for a given text_file.
def calc_frazier_score(tree, parent, parent_label):
    if type(tree) == str: return parent - 1
    else:
        count = 0
        for i, child in enumerate(tree):
            score = 0
            if i == 0:
                my_lab = tree.label()
                if is_sentence(my_lab): score = (0 if is_sentence(parent_label) else parent + 1.5)
                elif my_lab != "" and my_lab != "ROOT" and my_lab != "TOP": score = parent + 1
            count += calc_frazier_score(child, score, my_lab)
        return count


def get_yngve_score(text_file):
    sentences = 0
    total_yngve_score = 0
    trees = get_formatted_trees(text_file)
    for tree_line in trees:
        if tree_line.strip() == "":
            continue
        tree = Tree.fromstring(tree_line)
        words = get_word_score(tree)
        sentences += 1
        raw_ygnve_score = calc_yngve_score(tree, 0)
        mean_yngve_score = float(raw_ygnve_score) / words
        total_yngve_score += mean_yngve_score

    average_yngve_score = float(total_yngve_score) / sentences
    return average_yngve_score


def get_frazier_score(text_file):
    sentences = 0
    total_frazier_score = 0
    trees = get_formatted_trees(text_file)
    for tree_line in trees:
        if tree_line.strip() == "":
            continue
        tree = Tree.fromstring(tree_line)
        words = get_word_score(tree)
        sentences += 1
        raw_frazier_score = calc_frazier_score(tree, 0, "")
        mean_frazier_score = float(raw_frazier_score) / words
        total_frazier_score += mean_frazier_score

    average_frazier_score = float(total_frazier_score) / sentences
    return average_frazier_score
########################################################################################################################


##### DISFLUENCY-BASED FEATURES ########################################################################################
# Count the number of various disfluencies in a given text_file.
def count_disfluencies(text_file):
    global pause_count
    global break_count
    global total_disfluencies
    um_count = 0
    uh_count = 0
    ah_count = 0
    er_count = 0
    hm_count = 0
    rep_count = 0
    tokens = get_tokens(text_file)
    last_item = ''
    for item in tokens:
        if item == 'um':    um_count += 1
        elif item == 'uh':  uh_count += 1
        elif item == 'ah':  ah_count += 1
        elif item == 'er':  er_count += 1
        elif item == 'hm':  hm_count += 1

        if last_item == item:   rep_count += 1
        if item != '{SL}':      last_item = item

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


# Return a disfluency count for each individual utterance in csv format.
def get_disfluencies_per_utterance(text_file):
    utterances = get_utterances(text_file)
    count = 1
    output = ''
    last_item = ''
    for line in utterances:
        dis_count = 0
        other_count = 0
        word_count = 0
        for item in line.split():
            word_count += 1
            if item == '{SL}':
                dis_count += 1
            elif __normalize_word(item) in disfluency_list:
                dis_count += 1
                if __normalize_word(item) != 'um' or __normalize_word(item) != 'uh':
                    other_count += 1
            elif re.match(r'^.*-$', item):
                dis_count += 1

            if last_item == item:
                dis_count = dis_count
                dis_count += 1

            if item != '{SL}':
                last_item = item

        output += ('\n' + str(count) + ',' + str(dis_count))
        count += 1

    return output
########################################################################################################################


##### PRINT ALL STATS ##################################################################################################
def get_stats(text_file):
    output = '\n' + text_file
    output += '\n##### BASIC STATS ###############################################'
    output += '\nToken Count: ' + str(get_word_count(text_file))
    output += '\nType Count: ' + str(get_unique_word_count(text_file))
    output += '\nType-Token Ratio: ' + str(get_ttr(text_file))
    output += '\nUtterance Count: ' + str(get_num_utterances(text_file))
    output += '\nAverage Utterance Length: ' + str(get_avg_utterance_length(text_file))
    output += '\nTop 5 Words: ' + str(get_most_frequent(text_file, 5))
    output += '\n\n##### DISFLUENCY STATS ##########################################'
    output += '\n' + str(count_disfluencies(text_file))
    output += '\n\n##### ADVANCED STATS ############################################'
    output += '\nAverage Disfluencies per Utterance: ' \
              + str(float(total_disfluencies) / get_num_utterances(text_file))
    output += '\nDisfluency-Word Ratio: ' + str(float(total_disfluencies) / get_word_count(text_file))

    return output
########################################################################################################################


##### JUST PRINTING FUNCTIONS ##########################################################################################
# Print the Command List to stdout.
def display_command_list():
    print 'command\t\targ1\t\targ2\tdescription\t\t\t\t'
    for item in collections.OrderedDict(sorted(command_info.items())):
        print colored(item, 'green')\
              + colored(command_args[item], 'blue')\
              + colored('\t' + command_info[item], 'yellow')
    print '\n\t\t\t\t' + colored('*', 'red') + colored('\tDenotes an Optional Argument', 'yellow')
    return ''


# Print the Usage Instructions to stdout.
def print_usage_instructions():
    usage =  '\nInvalid command. For a list of available commands, use ' + colored('--commands', 'green') + '.'
    usage += '\nCommands look like this: ' + colored('claap', 'red') + ' ' + colored('COMMAND', 'green') + ' ' \
             + colored('*', 'red') + colored('arg1', 'blue') + ' ' + colored('*', 'red') + colored('arg2', 'blue') \
             + ' ' + colored('filename', 'yellow')
    usage += '\n' + colored('*', 'red') + ' denotes an optional argument.'
    usage += '\n\n' + colored('Warning:', 'red') + ' Large inputs, such as Moby Dick, will take longer to process.'

    print(usage)
    return ''


# Print the program info to stdout.
def info(opt = None):
    prog_info = '#################################################################'
    prog_info += '\n# CLAAP - Corpus & Linguistics Annotating & Analyzing in Python #'
    prog_info += '\n# Version 1.00 \tJune 24, 2015 \t04:24 PM UTC \t\t\t#'
    prog_info += '\n# Developed by Benjamin S. Meyers\t\t\t\t#'
    prog_info += '\n#\t\t\t\t\t\t\t\t#'
    prog_info += '\n# This application may not be copied, altered, or distributed \t#'
    prog_info += '\n# without written consent from the product owner. \t\t#'
    prog_info += '\n# \t\t\t\t\t\t\t\t#'
    prog_info += '\n# For documentation, visit: https://github.com/meyersbs/CLAAP \t#'
    prog_info += '\n# \t\t\t\t\t\t\t\t#'
    prog_info += "\n# If you're happy and you know it, CLAAP your hands!\t\t#"
    prog_info += '\n#\t\t\t\t\t\t\t\t#'
    prog_info += '\n#################################################################'

    if opt is None:
        print(prog_info)
        return ''
    elif opt == '42':
        douglas = "\n           o o o   .-\'\"\"\"\'-.   o o o             DON\'T PANIC!"
        douglas += "\n           \\\|/  .'         '.  \|//"
        douglas += "\n            \-;o/             \o;-/"
        douglas += "\n            // ;               ; \\\\"
        douglas += "\n           //__; :.         .: ;__\\\\"
        douglas += "\n          `-----\\'.'-.....-'.'/-----'           444    2222222"
        douglas += "\n                 '.'.-.-,_.'.'                 4444   222   222"
        douglas += "\n                   '(  (..-'                  44 44         22"
        douglas += "\n      |              '-'                     44  44        22"
        douglas += "\n  |           |                             444444444     22"
        douglas += "\n |  |  |    |                                    44      22"
        douglas += "\n     |     |  |                                  44    222"
        douglas += "\n| |   |     %%%                                  44   222222222"
        douglas += "\n    ___    _\|/_         _%%_____"
        douglas += "\n\,-\' \'_|   \___/      __/___ \'   \\"
        douglas += "\n/\"\"----\'          ___/__  \'   \'\'  \__%__       __%____%%%___"
        douglas += "\n                 /   \" \'   _%__ \'   \'   \_____/____ \'  __ \" \\"
        douglas += "\n           __%%_/__\'\' __     \'   _%_\'_   \     \"\'    _%__ \'\' \_"
        douglas += "\n __/\__%%_/_/___\___ \'\'   \'_%_\"___   \"    \_%__ \'___\"     \"\'   \\"
        douglas += "\n/_________________\____\'_RIP Douglas___\"_______\_______\'_____\"__\\"
        # douglas +="\n"
        print(douglas)
        return ''
    else:
        print_usage_instructions()
        return ''


# Print most recent version of CLAAP.
def version_info():
    print(versions[0])
    return ''


# Print help info.
def print_help(command = None):
    output = '\n' + colored('command', 'green')\
             + colored('\t\targ1\t\targ2', 'blue')\
             + colored('\tdescription', 'yellow')
    if command is None:
        output += '\n' + colored('--commands', 'green') + colored('\t\t\t\t' + command_info['--commands'], 'yellow')
        output += '\n' + colored('--info', 'green') + colored('\t\t\t\t\t' + command_info['--info'], 'yellow')
        output += '\n' + colored('--usage', 'green') + colored('\t\t\t\t\t' + command_info['--usage'], 'yellow')
        output += '\n' + colored('--version', 'green') + colored('\t\t\t\t' + command_info['--version'], 'yellow')
    elif command in command_info.keys():
        output += '\n' + colored(command, 'green')\
                  + colored(command_args[command], 'blue')\
                  + colored('\t' + command_info[command], 'yellow')
    return output
########################################################################################################################
