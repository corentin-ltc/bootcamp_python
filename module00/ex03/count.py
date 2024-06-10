
import sys
import string

def ispunct(char):
	punctmark = string.punctuation
	return char in punctmark

def text_analyzer(string_input):
	"""
    Analyzes a text string and prints information about its characters.

    Parameters:
    input_str (str): The text string to be analyzed.

    Returns:
    None
    """
	upper_letters = 0
	lower_letters = 0
	punct_marks = 0
	spaces = 0
	if not string_input:
		print("Error: No argument.")
		return
	if not isinstance(string_input, str):
		print("Error: The argument is not a string.")
		return
	print('The text contains %d character(s):' % len(string_input))
	for i in string_input:
		if (i.isupper()):
			upper_letters += 1
		if (i.islower()):
			lower_letters += 1
		if (ispunct(i)):
			punct_marks += 1
		if (i.isspace()):
			spaces += 1
	print('%d upper letter(s)' % upper_letters)
	print('%d lower letter(s)' % lower_letters)
	print('%d punctuation mark(s)' % punct_marks)
	print('%d space(s)' % spaces)
def main():
	if len(sys.argv) != 2:
		print('Erro: Too many arguments.')
		return
	text_analyzer(sys.argv[1])
main()

