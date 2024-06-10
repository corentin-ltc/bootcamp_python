
import sys

def main():
	if len(sys.argv) > 2:
		print('AssertionError: more than one argument are provided')
		return
	if len(sys.argv) < 2:
		print('No argument is provided')
		return
	try:
		integer_num = int(sys.argv[1])
	except:
		print('AssertionError: argument is not an integer')
		return
	if integer_num == 0:
		print('I\'m Zero.')
		return
	if integer_num % 2 == 0:
		print('I\'m Even.')
	else:	
		print('I\'m Odd.')
main()