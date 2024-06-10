
import sys

def main():
	if len(sys.argv) != 3:
		print('Error')
		return
	try:
		num1 = int(sys.argv[1])
		num2 = int(sys.argv[2])
	except:
		print('Error')
		return
	print('Sum:		', num1 + num2)
	print('Difference:	', num1 - num2)
	print('Product:	',num1 * num2)
	if not (num2):
		print('Quotient:	 ERROR (division by zero)\nRemainder:	 ERROR (modulo by zero)')
		return
	print('Quotient:	', num1 / num2)
	print('Remainder:	', num1 % num2)
main()