import re

def print_word_count(text_file):

	word_count = 0
	list_words = []
	with open(text_file) as f:
		for line in f:
			line.replace('  ', ' ')
			line.replace('\n', '')
			word_line = line.split()
			for word in word_line:
				list_words.append(word.strip(' \n'))

		marker_count = 0
		for word in list_words:
			if re.search(r'{SL}', word):
				marker_count+=1
			elif re.search(r'{NS}', word):
				marker_count+=1
			elif re.search(r'{BR}', word):
				marker_count+=1
			elif re.search(r'{LS}', word):
				marker_count+=1
			else:
				marker_count = marker_count
	print(str(len(list_words)) + ' - ' + str(marker_count))
	print(str(text_file) + ' : ' + str(len(list_words)-marker_count))

print_word_count('TD2_T2_Stereo.txt')
print_word_count('TD2_T2_Stereo_UB.txt')

