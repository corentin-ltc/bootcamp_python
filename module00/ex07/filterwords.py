
import sys
import string

words_lib = {
	'accepted_words' : (""),
}

def main():
	if len(sys.argv) != 3:
		print("Error")
		return
	words = sys.argv[1].split()
	try:
		n_min = int(sys.argv[2])
	except:
		print("Error: Second argument is not an integer")
		return
	new_list = []
	for word in words:
		word = word.translate(str.maketrans('', '', string.punctuation))
		if len(word) > n_min:
			new_list.append(word)
	words_lib['accepted_words'] = (new_list)
	print(words_lib['accepted_words'])
main()
