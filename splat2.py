
import sys, os
if sys.version_info <= (2, 7):	import cPickle as pkl
else:							import pickle as pkl
from base.TextBubble import TextBubble
from base import Util

my_bubble = None
commands = {}

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
				"drawtrees":Util.drawtrees}

def main():
	args = sys.argv
	if len(args) < 2:
		sys.exit("WARNING: Invalid input. Try '--help' for more details.")
	else:
		load_bubble(args)
		setup_commands()
		run_command(args[:-1])

if __name__ == "__main__":
	main()