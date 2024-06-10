
import sys


def print_reverse(input_str):
	input_str = input_str [::-1]
	print (input_str.swapcase())
def main():
	if len(sys.argv) > 1:
		input_str = ""
	if len(sys.argv) < 2:
		print('Error')
		return
	j = 1
	while j <= (len(sys.argv) - 1):
		input_str += sys.argv[j]
		j += 1
		if j != len(sys.argv):
			input_str += " "
	print_reverse(input_str)

main()