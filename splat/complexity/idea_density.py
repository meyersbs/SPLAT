import sys, re

########################################################################################################################
##### INFORMATION ######################################################################################################
### @PROJECT_NAME:		SPLAT: Speech Processing and Linguistic Analysis Tool										 ###
### @VERSION_NUMBER:																								 ###
### @PROJECT_SITE:		github.com/meyersbs/SPLAT																     ###
### @AUTHOR_NAME:		Benjamin S. Meyers																			 ###
### @CONTACT_EMAIL:		ben@splat-library.org																		 ###
### @LICENSE_TYPE:		MIT																							 ###
########################################################################################################################
########################################################################################################################

##### GLOBAL VARIABLES #################################################################################################

global ADJ, ADV, VERB, NOUN, INTERR, PROP, FILLER, BE, NT, COMEGO, AUX
global BEING, BECOMING, SEEMING, LINKING, CLINKING, CORREL, NEGPOL1, NEGPOL2

##### WORD CLASSES #####################################################################################################

ADJ = ["JJ", "JJR", "JJS"]
ADV = ["RB", "RBR", "RBS", "WRB"]
VERB = ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ", "BES"]
NOUN = ["NN", "NNS", "NNP", "NNPS"]
INTERR = ["WDT", "WP", "WPS", "WRB"]

# By default, words classified as one of these parts-of-speech is considered a proposition.
PROP = ADJ + ADV + VERB + INTERR + ["CC", "CD", "DT", "IN", "PDT", "POS", "PRP$", "PP$", "TO"]

# A sentence consisting wholly of 'non-propositional fillers' is considered to be propositionless.
FILLER = ["and", "or", "but", "if", "that", "just", "you", "know"]

# All forms of 'be'.
BE = ["am", "is", "are", "was", "were", "being", "been"]

# Common negative contractions that may slip through the tagger, especially if accidentally typed without an apostrophe.
NT = ["didn't", "didnt", "don't", "dont", "can't", "cant", "couldn't", "couldnt", "won't", "wont", "wouldn't",
	  "wouldnt"]

# "Come", "go", and their synonyms form a single proposition with following "to" or "from".
COMEGO = ["come", "comes", "came", "coming", "return", "returns", "returned", "returning", "arrive", "arrives",
		  "arrived", "arriving", "go", "goes", "went", "gone", "going", "depart", "departs", "departed", "departing",
		  "emanate", "emanates", "emanated", "emanating"]

# All forms of all auxiliary verbs. NOTE: "needs", "dares", "doing" and "done" are not auxiliary forms.
AUX = ["be", "am", "is", "are", "was", "were", "being", "been", "have", "has", "had", "having", "do", "does", "did",
	   "need", "dare"]

# Being
BEING = ["be", "am", "is", "are", "was", "were", "been", "being"]
# Becoming
BECOMING = ["become", "becomes", "became", "becoming", "get", "gets", "got", "gotten", "getting"]
# Seeming
SEEMING = ["look", "looks", "looked", "looking", "seem", "seems", "seemed", "seeming", "appear", "appears", "appeared",
		   "appearing", "sound", "sounds", "sounded", "sounding", "feel", "feels", "felt", "feeling", "smell", "smells",
		   "smelled", "smelling", "taste", "tastes", "tasted", "tasting"]

# All forms of linking verbs that precede an adjective.
LINKING = BEING + BECOMING + SEEMING

# Causative linking verbs: all forms of all verbs that take noun phrase + adjective after them, such as "make it better"
# or "turn it green."
CLINKING = ["make", "makes", "made", "making", "turn", "turns", "turned", "turning", "paint", "paints", "painted",
			"painting"]

# The first elements of coordinating conjunctions.
CORREL = ["both", "either", "neither"]

# NOTE: The following are not all the negative-polarity items of English, but only the ones that seem to form 2-word
# 1-concept idioms.

# Negative-polarity terms where the negation of this word counts as a proposition. For example: "not...yet" = "not".
NEGPOL1 = ["yet", "much", "many", "any", "anymore"]

# Negative-polarity terms where this word (not its negation) counts as a proposition.
NEGPOL2 = ["unless"]

# Punctuation.
PUNCT = [":", ",", "."]

########################################################################################################################

class WordObj:
	""" Helper class for organizations features associated with a word. """
	def __init__(self, token="", tag="", isprop=False, isword=False, rulenumber=0):
		""" Constructor. """
		self.token = token
		self.tag = tag
		self.isprop = isprop
		self.isword = isword
		self.rulenumber = rulenumber

#### HELPER FUNCTIONS ##################################################################################################

def contains(array_name, item):
	""" Returns True if the given array contains the given item. Otherwise, returns False. """
	try: return array_name.index(item)
	except ValueError: return False

def sent_beginning(word_list, i):
	""" Returns the first word in the given list containing the given word. """
	j = i - 1
	while (j > 0) and (word_list[j].tag != ".") and (word_list[j].tag != ""): j -= 1
	return j + 1

def likely_repetition(first_string, second_string):
	"""
	Determines whether a given word is a likely repetition of the other given word. For example, the first word may be
	incomplete: "hesi- hesitation".
	"""
	if len(first_string) == 0 or len(second_string) == 0: return False
	if first_string == second_string: return True
	if first_string[-1] == "-": first_string = first_string[0:-1]
	if len(second_string) > 3 and first_string != "a" and first_string != "an" \
		and second_string[0:len(first_string)] == first_string: return True

	return False

##### RULES FOR IDEA-COUNTING ##########################################################################################

def apply_counting_rules(word_list, speech_mode=False):
	"""
	Apply all of the idea-counting rules to the given list of words.

	Rules are numbered, but rule numbering is not consecutive, leaving room for more rules to be added to their
	respective groups in the future. The most recent rule to act on each word is identified by the "rulenumber" field in
	the WordObj.

	The parameter "speech_mode" defaults to False. Some rules only apply if "speech_mode" is True. It should be set to
	True when analyzing transcribed speech that contains repetitions and filler words. It may result in undercounting
	of well-edited English.
	"""
	global ADJ, ADV, VERB, NOUN, INTERR, PROP, FILLER, BE, NT, COMEGO, AUX, BEING, BECOMING, SEEMING, LINKING,\
		CLINKING, CORREL, NEGPOL1, NEGPOL2, PUNCT

	"""
	The following loop iterates over every word in the given list of words; it may add and/or remove words. The rules
	refer back to the beginning of the current word; in other words, rules are triggered by the last word matching the
	pattern it is looking for. It is guaranteed that there will be 10 null items at the beginning of the given list of
	words; rules do not have to worry about going past the beginning of the list.

	The majority of rules depend on the output of prior rules (see rule 200 for a good example). The algorithm could be
	made more efficient by identifying rules that DO NOT feed a subsequent rule, and putting a "continue" statement in
	them (see rule 000 for an example).

	Additions and deletions to the given word list take place AFTER the current location. For example, if the current
	word is at index 'i', additions and deletions may occur at index 'i+1', but not at index 'i-1'. This prevents
	renumbering. Rules 003 and 004 contain examples of stepping backward and deleting forward.

	Deletion removes the item from both the word count and the idea count; accordingly, items should only be deleted if
	they have been moved or should not be counted as words.
	"""
	i = -1
	while i < len(word_list) - 1:
		i += 1
		##### RULE GROUP 000 - Identify Words and Adjust Tags ##########################################################

		##### RULE 000 #####
		## If it's a null item, skip the rest of these tests. There will always be at least 10 null items at the
		## beginning so we can freely look back from the current position without running off the beginning of the list.
		if word_list[i].token == "": continue

		##### RULE 001 #####
		## The symbol '^' is used to mark broken-off spoken sentences.

		# NOTE: I have chosen to ignore this rule because it does not seem to apply to the sorts of input SPLAT is
		#       expecting.

		##### RULE 002 #####
		## The item is a word if its token starts with a letter or digit and its tag is not SYM (symbol).
		if re.search("[\d\w]", word_list[i].token) and word_list[i].tag != "SYM":
			word_list[i].isword = True
			word_list[i].rulenumber = 2

		##### RULE 003 #####
		## Two cardinal numbers in immediate succession are combined into one. This is very uncommon.
		if word_list[i].tag == "CD" and i > 0:
			if word_list[i-1].tag == "CD":
				# adjust token
				word_list[i-1].token = word_list[i-1].token + " " + word_list[i].token
				word_list[i-1].rulenumber = 3
				i -= 1 # step backward 1
				word_list.pop(i+1) # delete forward 1

		##### RULE 004 #####
		## Handling of factions, decimals, etc. If the current token is a number, the preceding token contains some
		## characters, the first of which is nonalphanumeric and the pre-preceding token is also a number, adjust.
		if word_list[i].tag == "CD" and len(word_list[i-1].token) > 0 and not re.search("[\d\w]", word_list[i-1].token)\
			and word_list[i-2].tag == "CD":
			word_list[i-2].token = word_list[i-2].token + word_list[i-1].token + word_list[i].token
			word_list[i-2].rulenumber = 4
			i -= 2  # step backward 2
			word_list.pop(i + 1) # delete forward 1
			word_list.pop(i + 1) # delete forward 1

		##### RULE 020 #####
		## Repetition of the form "A A" is simplified to "A". The first "A" can be an initial substring of the second
		# one. Both remain in the word count.
		if speech_mode:
			if likely_repetition(word_list[i - 1].token, word_list[i].token):
				# Mark the first A as to be ignored
				word_list[i-1].isprop = False
				word_list[i-1].isword = False
				word_list[i-1].tag = ""
				word_list[i-1].rulenumber = 20

		##### RULE 021 #####
		## Repetition of the form "A Punctuation A" is simplified to "A". Both "A"s remain in the word count. The first
		## "A" may be an initial substring of the second one. Punctuation is anything tagged ".", ",", or ":".
		##### RULE 022 #####
		## Repetition of the form "A B A" is simplified to "A B". Both "A"s remain in the word count. The first A may
		## be an initial substring of the second one.

		if speech_mode:
			if likely_repetition(word_list[i-2].token, word_list[i].token) and not contains(PUNCT, word_list[i].tag):
				# Mark the first A to be ignored
				word_list[i-2].tag = ""
				word_list[i-2].isword = False
				word_list[i-2].isprop = False
				word_list[i-2].rulenumber = 22
				# Mark the punctuation mark to be ignored
				if contains(PUNCT, word_list[i-1].tag):
					word_list[i-1].tag = ""
					word_list[i-1].isword = False
					word_list[i-1].isprop = False
					word_list[i-1].rulenumber = 21

		##### RULE 023 #####
        ## Repetition of the form "A B Punctuation A B" is simplified to "A B". Both "A"s and "B"s remain in the word
		## count. The first "A" (or "B") can be an initial substring of the second one. Punctuation is anything with tag
		## ".", ",", or ":".

		if speech_mode:
			if likely_repetition(word_list[i-3].token, word_list[i].token) \
				and likely_repetition(word_list[i-4].token, word_list[i-1].token) \
				and (word_list[i-2].tag == "." or word_list[i-2].tag == "," or word_list[i-2].tag == ":"):
				word_list[i-4].tag = word_list[i-3].tag = word_list[i-2].tag = ""
				word_list[i-4].isword = word_list[i-3].isword = word_list[i-2].isword = False
				word_list[i-4].isprop = word_list[i-3].isprop = word_list[i-2].isprop = False
				word_list[i-4].rulenumber = word_list[i-3].rulenumber = word_list[i-2].rulenumber = 23

		##### RULE 050 #####
		## 'not' and any word ending in "n't" are not putatively propositions and their tag is changed to NOT.
		if word_list[i].token == "not" or word_list[i].token[-3:] == "n't" or contains(NT, word_list[i].token):
			word_list[i].isprop = True
			word_list[i].tag = "NOT"
			word_list[i].rulenumber = 50

		##### RULE 054 #####
		## "that/DT" or "this/DT" is a pronoun, not a determiner, if the following word is a verb or an adverb.
		if (word_list[i-1].token == "that" or word_list[i-1].token == "this") and (contains(VERB, word_list[i].tag) or
			contains(ADV, word_list[i].tag)):
			word_list[i - 1].tag = "PRP"
			word_list[i - 1].rulenumber = 54
			word_list[i - 1].isprop = False

		# TODO: Pick up here.
		## Rule group 100 - Word order adjustment
		# Since all the rules apply in one pass,
		# this must be approached carefully.

		# 101
		# Subject-Aux inversion
		""" If the current word is an Aux,
			and the current word is the first word of the sentence
				or the sentence begins with an interrogative,
				move the current word rightward to put it in front
				of the first verb, or the end of the sentence.
				In some cases this will move a word too far to the right,
				but the effect on proposition counting is benign.
		"""
		if contains(AUX, word_list[i].token):
			bos = sent_beginning(word_list, i)
			if bos == i or contains(INTERR, word_list[bos].tag):
				# find out where to move to
				dest = i
				# Is this right?
				while dest < len(word_list) - 1:
					dest += 1
					if word_list[dest].tag == "." \
							or contains(VERB, word_list[dest].tag):
						break
				# if movement is called for,
				if dest > (i + 1):
					# insert a copy in the new location
					word_list.insert(dest, WordObj(word_list[i].token, word_list[i].tag, True, True, 101))
					# mark the old item as to be ignored
					word_list[i].tag = ""
					word_list[i].isprop = False
					word_list[i].isword = False
					word_list[i].token += "/moved"


				## Rule group 200 - Preliminary identification of propositions ##

		# 200
		# The tags in Prop are taken to indicate propositions.
		if contains(PROP, word_list[i].tag):
			word_list[i].isprop = True
			word_list[i].rulenumber = 200

		# 201
		# 'The', 'a', and 'an' are not propositions.
		if word_list[i].token == "the" or word_list[i].token == "an" or word_list[i].token == "a":
			word_list[i].isprop = False
			word_list[i].rulenumber = 201

		# Better agreement with Turner & Greene without this rule.
		# 202
		# //// An attriword_listutive noun (such as 'lion' in 'lion tamer') is a proposition
		# //// (like an adjective).
		# //if (Contains(Noun, word_list[i].tag) and (word_list[i - 1].tag == "NN"))
		# //{
		# //  word_list[i - 1].isprop = True;
		# //  word_list[i - 1].rulenumber = 202;
		# //}


		# 203
		""" The first word in a correlating conjunction such as
				"either...or", "neither...nor", "both...and"
			is not a proposition. The second word is tagged CC;
				the first word may have been tagged CC, RB, or DT.
		NB:  "nor" is tagged as RB once in the SWBD corpus!!
		"""
		if word_list[i].tag == "CC" and not contains(CORREL, word_list[i].token):
			# Search back up to 10 words, but not across a sentence end.
			# In our case, this is true if i = 0
			j = i
			while j > i - 10:
				j -= 1
				# if word_list[j].tag == ".":
				if j == -1:
					break
				if contains(CORREL, word_list[j].token):
					word_list[j].isprop = False
					word_list[j].rulenumber = 203
					break

		# 204
		"""  "And then" and "or else" are each a single proposition """
		if word_list[i - 1].token == "and" and word_list[i].token == "then" or \
								word_list[i - 1].token == "or" and word_list[i].token == "else":
			word_list[i].isprop = False
			word_list[i].rulenumber = 204

		# 206
		""" "To" is not a proposition when it is last word in sentence. """
		if word_list[i].tag == "." and word_list[i - 1].tag == "TO":
			word_list[i - 1].isprop = False
			word_list[i - 1].rulenumber = 206

		# 207
		""" Modal is a proposition when it is last word in sentence. """
		if word_list[i].tag == "." and word_list[i - 1].tag == "MD":
			word_list[i - 1].isprop = True
			word_list[i - 1].rulenumber = 207

		# 210
		""" Cardinal number is a proposition only if there is a noun
			within 5 words after it (not crossing a sentence boundary).
			This is so "in 3 parts" is 2 props but "in 1941" is only one.
		"""
		if word_list[i].tag == "CD":
			word_list[i].isprop = False
			word_list[i].rulenumber = 210
			# This rule looks forward up to 5 words, but not past
			# an end-of-sentence marker or the end of the WordList.
			j = i
			while (j < (len(word_list) - 1) and j < i + 6):
				j += 1
				# if word_list[j].tag == ".":
				if j == -1:
					break
				if contains(NOUN, word_list[j].tag):
					word_list[i].isprop = True
					break
		# 211
		""" 'Not...unless' and similar pairs count as one proposition
				(the second word is the one counted).
		"""
		if contains(NEGPOL2, word_list[i].token):
			# Much the same algorithm as for correlating conjunctions.
			# Search back up to 10 words, but not across a sentence end.
			j = i
			while i > i - 10:
				j -= 1
				# if word_list[j].tag == ".":
				if j == -1:
					break
				if word_list[j].tag == "NOT":
					word_list[j].isprop = False
					word_list[j].rulenumber = 211
					break

		# 212
		""" 'Not...any' and similar pairs count as one proposition
			(the first word is the one counted).
		"""
		if contains(NEGPOL1, word_list[i].token):
			# Much the same algorithm as for correlating conjunctions.
			# Search back up to 10 words, but not across a sentence end.
			j = i
			while j > i - 10:
				j -= 1
				# if word_list[j].tag == ".":
				if j == -1:
					break
				if word_list[j].tag == "NOT":
					word_list[i].isprop = False
					word_list[i].rulenumber = 212
					break

		# 213
		""" "Going to" is not a proposition when immediately preceding a verb. """
		if contains(VERB, word_list[i].tag) and word_list[i - 1].token == "to" and \
						word_list[i - 2].token == "going":
			word_list[i - 1].isprop = False
			word_list[i - 1].rulenumber = 213
			word_list[i - 2].isprop = False
			word_list[i - 2].rulenumber = 213

		# 214
		""" "If ... then" is 1 conjunction, not two.
			Actually checking for "if ... then (word)"
			because "then" as last word of sentence is more likely to be adverb.
		"""
		if word_list[i].isword and word_list[i - 1].token == "then":
			# Much the same algorithm as for correlating conjunctions.
			# Search back up to 10 words, but not across a sentence end.
			j = i
			while j > i - 10:
				j -= 1
				# if word_list[j].tag == ".":
				if j == -1:
					break
				if word_list[j].token == "if":
					word_list[i - 1].isprop = False
					word_list[i - 1].rulenumber = 214
					break

		# 225
		""" "each other" is a pronoun (to be tagged as PRP PRP). """
		if word_list[i].token == "other" and word_list[i - 1].token == "each":
			word_list[i].tag = word_list[i - 1].tag = "PRP"
			word_list[i].isprop = word_list[i - 1].isprop = False
			word_list[i].rulenumber = word_list[i - 1].rulenumber = 225

		# 230
		""" "how come" and "how many" are each 1 proposition, not two. """
		if (word_list[i].token == "come" or word_list[i].token == "many") \
				and word_list[i - 1].token == "how":
			word_list[i].isprop = False
			word_list[i].tag = word_list[i - 1].tag
			word_list[i].rulenumber = 230

		### Rule group 300 - Linking verbs ###

		# 301
		""" A linking verb is not a proposition if followed by adj. or adv.
				(Apparently, adverbs are frequent tagging mistakes for adjectives.)
		"""
		if (contains(ADJ, word_list[i].tag) or contains(ADV, word_list[i].tag)) \
				and contains(LINKING, word_list[i - 1].token):
			word_list[i - 1].isprop = False
			word_list[i - 1].rulenumber = 301

		# 302
		""" "Be" is not a proposition when followed by a preposition.
				(May want to modify this to allow an intervening adverb.)
		"""
		if word_list[i].tag == "IN" and contains(BE, word_list[i - 1].token):
			word_list[i - 1].isprop = False
			word_list[i - 1].rulenumber = 302

		# 310
		""" Linking verb + Adverb + { PDT, DT } is 2 propositions
			(e.g., "he is now the president").
				   (Would otherwise be undercounted because of rule 201).
		"""
		if word_list[i].tag == "DT" or word_list[i].tag == "PDT":
			if contains(ADV, word_list[i - 1].tag) and contains(LINKING, word_list[i - 2].token):
				word_list[i - 1].isprop = True
				word_list[i - 1].rulenumber = 310
				word_list[i - 2].isprop = True
				word_list[i - 2].rulenumber = 310

		# 311
		""" Causative linking verbs: 'make it better' and similar
			phrases do not count the adjective as a new proposition
			(since the verb was counted).
		"""
		if contains(ADJ, word_list[i].tag):
			# Much the same algorithm as for correlating conjunctions.
			# Search back up to 10 words, but not across a sentence end.
			j = i
			while j > i - 10:
				j -= 1
				# if word_list[j].tag == ".":
				if j == -1:
					break
				if contains(CLINKING, word_list[j].token):
					word_list[i].isprop = False
					word_list[i].rulenumber = 311
					break

		## Rule group 400 - Auxiliary verbs are not propositions ##

		# Note that VERB is a list of tags but AUX is a list of tokens.
		# Note also that VERB includes all AUX.

		# 401
		""" "Aux not" is one proposition, not two """
		if word_list[i].token == "not" and contains(AUX, word_list[i - 1].token):
			word_list[i - 1].isprop = False
			word_list[i - 1].rulenumber = 401

		# 402
		""" "Aux Verb" is one proposition, not two """
		if contains(VERB, word_list[i].tag) and contains(AUX, word_list[i - 1].token):
			word_list[i - 1].isprop = False
			word_list[i - 1].rulenumber = 402

		# 405
		""" "Aux NOT Verb"        (NOT and the second Verb are propositions)
			Also "Aux Adverb Verb"  (e.g., "had always sung", "would rather go")
		"""
		if contains(VERB, word_list[i].tag) and (word_list[i - 1].tag == "NOT" \
														 or contains(ADV, word_list[i - 1].tag)) \
				and contains(AUX, word_list[i - 2].token):
			word_list[i - 2].isprop = False
			word_list[i - 2].rulenumber = 405

		## Rule group 500 - Constructions involving 'to' ##

		# 510
		""" "TO VB" is one proposition, not two """
		if ((word_list[i].tag == "VB") and (word_list[i - 1].tag == "TO")):
			word_list[i - 1].isprop = False
			word_list[i - 1].rulenumber = 510

		# 511
		""" "for ... TO VB": "for" is not a proposition """
		if ((word_list[i].tag == "VB") and (word_list[i - 1].tag == "TO")):
			# Search back up to 10 words, but not across a sentence end.
			j = i
			while j > i - 10:
				j -= 1
				# if word_list[j].tag == ".":
				if j == -1:
					break
				if (word_list[j].token == "for"):
					word_list[j].isprop = False
					word_list[j].rulenumber = 511
					break
		# 512
		""" "From" and "to" form a single proposition with
			preceding "go", "come", or their synonyms.
			(Better agreement with Turner & Greene without this rule.) """
		# if ((word_list[i].token == "to") or (word_list[i].token == "from")) and \
		#   (Contains(COMEGO, word_list[i - 1].token) or Contains(COMEGO, word_list[i - 2].token)):
		# //   )
		# //{
		# //  word_list[i].isprop = False;
		# //  word_list[i].rulenumber = 512;
		# //}


		## Rule group 600 - Fillers ##

		# 610
		""" A sentence consisting entirely of probable filler words is propositionless """
		if (speech_mode and word_list[i].tag == "."):
			bos = sent_beginning(word_list, i)
			k = 0
			j = bos
			while j < i:
				if ((word_list[j].tag != "UH") and not contains(FILLER, word_list[j].token)):
					k += 1
				j += 1
			if (k == 0):
				j = bos
				while j < i:
					word_list[j].tag = ""
					word_list[j].isprop = False
					word_list[j].rulenumber = 610
					j += 1
		# 632
		""" In speech mode, "like" is a filler when not immediately preceded by a form of "be". """
		if (speech_mode):
			if ((word_list[i].token == "like") and not contains(BE, word_list[i - 1].token)):
				word_list[i].tag = ""
				word_list[i].isprop = False
				word_list[i].rulenumber = 632

		# 634
		""" In speech mode, "you know" is a filler and counts as one word, not two. """
		if (speech_mode):
			if ((word_list[i - 1].token == "you") and (word_list[i].token == "know")):
				# back up one
				i -= 1
				# delete forward one
				word_list.pop(i + 1)
				# reset data for the current item
				word_list[i].token = "you_know"
				word_list[i].tag = ""
				word_list[i].isprop = False
				word_list[i].isword = True
				word_list[i].rulenumber = 634
	# end for
	return word_list

def calc_propositions(word_list):
	""" Returns the number of propositions in the given list of words. """
	props = 0
	for word in word_list:
		if word.isprop:
			props += 1
	return props

def calc_idea(treestrings):
	"""
	Calculate the idea density (also known as proposition density or p-density).

	Idea density is the ratio of expressed propositions words to total words. Word classes are determined by the
	part-of-speech tags assigned by the Berkeley Parser. The categorization of POS tags and the algorithm used to
	calculate idea density is based on the work of Margaret Mitchell and Kristy Hollingshead, under the guidance of
	Brian Roark. For questions or concerns regarding this calculation, please contact Margaret Mitchell
	(m.mitchell@abdn.ac.uk) or Brian Roark (roark@cslu.ogi.edu), or consult the following publications:

		Brian Roark, Margaret Mitchell, John-Paul Hosom, Kristy Hollingshead and Jeffrey A. Kaye. 2011. Spoken language
			derived measures for detecting Mild Cognitive Impairment. IEEE Transactions on Audio, Speech and Language
			Processing, 19(8).

		Brian Roark, Margaret Mitchell and Kristy Hollingshead. 2007. Syntactic complexity measures for detecting Mild
			Cognitive Impairment. In Proceedings of the ACL 2007 Workshop on Biomedical Natural Language Processing
			(BioNLP), pp. 1-8.

		Brian Roark, John-Paul Hosom, Margaret Mitchell and Jeffrey A. Kaye. 2007. Automatically derived spoken language
			markers for detecting Mild Cognitive Impairment. In Proceedings of the 2nd International Conference on
			Technology and Aging (ICTA).
	"""
	results = []
	for utterance in treestrings:
		word_list = []
		tags_tokens = re.findall("\((\S+) ([^\(^\)]+)\)", utterance)
		num_words = float(len(tags_tokens))
		for (tag, token) in tags_tokens:
			word = WordObj()
			word.token = token
			word.tag = tag
			word_list += [word]
		word_list = apply_counting_rules(word_list)
		props = calc_propositions(word_list)
		p_density = (float(props)) / float(num_words)
		results.append(p_density)

	# return (mean, min, max) idea density
	return float(sum(results)/len(results)), float(min(results)), float(max(results))
