
import sys
import string


def isalnumorspace(text):
	for char in text:
		if (not char.isalnum() and not char.isspace()):
			return 0
	return 1

def main():
	
	morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.', '0': '-----',
        ' ': '/'
	}

	if len(sys.argv) != 2:
		print("Error")
		return
	if not isalnumorspace(sys.argv[1]):
		print("Error")
		return
	string_input = sys.argv[1]
	string_input = string_input.upper()
	encoded_text = []
	for char in string_input:
		if char in morse_code:
			encoded_text.append(morse_code[char])
	encoded_string = ' '.join(encoded_text)
	print(encoded_string)
main()
