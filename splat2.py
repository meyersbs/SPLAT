import sys
import os
import pickle

from base.TextBubble import TextBubble

my_bubble = None
commands = {}

def command_message():
	template = "{0:15}{1:15}{2:15}{3:100}"
	print(template.format("COMMAND", "ARG1", "ARG2", "DESCRIPTION"))
	print(template.format("als", "--", "<input_file>", "Display average sentence length."))
	print(template.format("alu", "--", "<input_file>", "Display average utterance length."))
	print(template.format("bigrams", "--", "<input_file>", "Display all bigrams."))
	print(template.format("cdensity", "--", "<input_file>", "Display content density."))
	print(template.format("cfr", "--", "<input_file>", "Display content-function ratio."))
	print(template.format("content", "--", "<input_file>", "Display all content words."))
	print(template.format("disfluencies", "--", "<input_file>", "Display all disfluency counts."))
	print(template.format("dps", "--", "<input_file>", "Display disfluencies per sentence."))
	print(template.format("dpu", "--", "<input_file>", "Display disfluencies per utterance."))
	print(template.format("drawtrees", "--", "<input_file>", "Draw syntactic parse trees."))
	print(template.format("frazier", "--", "<input_file>", "Display frazier score."))
	print(template.format("function", "--", "<input_file>", "Display all function words."))
	print(template.format("idensity", "--", "<input_file>", "Display idea density."))
	print(template.format("leastfreq", "<x>", "<input_file>", "Display the <x> least frequent words."))
	print(template.format("maxdepth", "--", "<input_file>", "Display maxdepth of trees."))
	print(template.format("mostfreq", "<x>", "<input_file>", "Display the <x> most frequent words."))
	print(template.format("ngrams", "<n>", "<input_file>", "Display all <n>-grams."))
	print(template.format("plotfreq", "--", "<input_file>", "Plot the <x> most frequent words."))
	print(template.format("pos", "--", "<input_file>", "Display tokens with POS tags."))
	print(template.format("poscounts", "--", "<input_file>", "Display counts for each POS tag."))
	print(template.format("sents", "--", "<input_file>", "Display sentences."))
	print(template.format("sentcount", "--", "<input_file>", "Display number of sentences."))
	print(template.format("tokens", "--", "<input_file>", "Display all tokens."))
	print(template.format("trees", "--", "<input_file>", "Display all parse trees."))
	print(template.format("trigrams", "--", "<input_file>", "Display all trigrams."))
	print(template.format("ttr", "--", "<input_file>", "Display type-token ratio."))
	print(template.format("types", "--", "<input_file>", "Display all types."))
	print(template.format("ufunction", "--", "<input_file>", "Display all unique function words."))
	print(template.format("unigrams", "--", "<input_file>", "Display all unigrams."))
	print(template.format("uttcount", "--", "<input_file>", "Display number of utterances."))
	print(template.format("utts", "--", "<input_file>", "Display utterances."))
	print(template.format("uwc", "--", "<input_file>", "Display unique wordcount."))
	print(template.format("wc", "--", "<input_file>", "Display wordcount."))
	print(template.format("wps", "--", "<input_file>", "Display words per sentence counts."))
	print(template.format("wpu", "--", "<input_file>", "Display words per utterance counts."))
	print(template.format("yngve", "--", "<input_file>", "Display yngve score."))

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
		my_bubble = pickle.load(open(args[-1] + ".pkl", 'rb'))
	else:
		my_bubble = TextBubble(args[-1])
		pickle.dump(my_bubble, open(args[-1] + ".pkl", 'wb'), protocol=2)

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
				"wps":my_bubble.words_per_sentence,			"utts":my_bubble.utts,
				"cdensity":my_bubble.content_density,		"idensity":my_bubble.idea_density,
				"yngve":my_bubble.yngve_score,				"frazier":my_bubble.frazier_score,
				"poscounts":my_bubble.pos_counts,			"maxdepth":my_bubble.max_depth,
				"mostfreq":my_bubble.get_most_freq,			"leastfreq":my_bubble.get_least_freq,
				"plotfreq":my_bubble.plot_freq,				"dpu":my_bubble.disfluencies_per_utterance,
				"dps":my_bubble.disfluencies_per_sentence,	"disfluencies":my_bubble.disfluencies,
				"als":my_bubble.average_sentence_length}

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
		elif args[1] == "--commands":
			command_message()
	else:
		load_bubble(args)
		setup_commands()
		run_command(args[:-1])

if __name__ == "__main__":
	main()