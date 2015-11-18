
import sys, os
if sys.version_info <= (2, 7):	import cPickle as pkl
else:							import pickle as pkl
from base.TextBubble import TextBubble
from base import Util

my_bubble = None
commands = {}

def usage_message():
	message = "USAGE: splat <command> <options> <text_source>"
	return message

def help_message():
	message = "USAGE: splat <command> <options> <text_source>\n"
	message += "\t--commands\tList available commands.\n"
	message += "\t--info\t\tDisplay licensing information.\n"
	return message

def info_message():
	prog_info = "#################################################################"
	prog_info += "\n# SPLAT - Speech Processing & Linguistic Annotation Tool \t#"
	prog_info += "\n# Copyright (C) 2015, Benjamin S. Meyers\t\t\t#"
	prog_info += "\n# \t\t\t\t\t\t\t\t#"
	prog_info += "\n# Developed by Benjamin S. Meyers in collaboration with:\t#"
	prog_info += "\n#\tEmily Prud'hommeaux\tCissi O. Alm\t\t\t#"
	prog_info += "\n#\tAndrew Carpenter\tBryan T. Meyers\t\t\t#"
	prog_info += "\n# \t\t\t\t\t\t\t\t#"
	prog_info += "\n# For documentation, visit: https://github.com/meyersbs/SPLAT \t#"
	prog_info += "\n#################################################################"
	return prog_info

def run_command(args):
	command = args[1]
	if command not in commands.keys():
		sys.exit("WARNING: Invalid command. Try '--help' for details.")
	if len(args) == 2: # splat <command>
		print(commands[command]())
	elif len(args) == 3: # splat <command> <option>
		print(commands[command](int(args[2])))

def load_bubble(args):
	global my_bubble
	if os.path.exists(args[-1] + ".pkl"):
		my_bubble = pkl.load(open(args[-1] + ".pkl", 'rb'))
	else:
		my_bubble = TextBubble(args[-1])
		pkl.dump(my_bubble, open(args[-1] + ".pkl", 'wb'), protocol=2)

def setup_commands():
	global commands
	commands = {"wc":my_bubble.wordcount, 					"uwc":my_bubble.unique_wordcount,
				"tokens":my_bubble.tokens, 					"types":my_bubble.types,
				"sents":my_bubble.sents, 					"sentcount":my_bubble.sentcount,
				"ttr":my_bubble.type_token_ratio,			"ngrams":my_bubble.ngrams,
				"pos":my_bubble.pos,						"alu":my_bubble.average_utterance_length,
				"cfr":my_bubble.content_function_ratio,		"uttcount":my_bubble.uttcount,
				"unigrams":my_bubble.unigrams,				"bigrams":my_bubble.bigrams,
				"trigrams":my_bubble.trigrams,				"content":my_bubble.content_words,
				"function":my_bubble.function_words,		"ucontent":my_bubble.unique_content_words,
				"ufunction":my_bubble.unique_function_words,"trees":my_bubble.treestrings,
				"drawtrees":my_bubble.drawtrees,			"wpu":my_bubble.words_per_utterance,
				"wps":my_bubble.words_per_sentence,			"utts":my_bubble.utts}

def main():
	args = sys.argv
	if len(args) < 2:
		sys.exit("WARNING: Invalid input. Try '--help' for more details.")
	elif len(args) == 2:
		if args[1] == "--help":
			print(help_message())
		elif args[1] == "--info":
			print(info_message())
		elif args[1] == "--usage":
			print(usage_message())
	else:
		load_bubble(args)
		setup_commands()
		run_command(args[:-1])

if __name__ == "__main__":
	main()