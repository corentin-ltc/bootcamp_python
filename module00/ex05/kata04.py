kata = (0, 4, 132.42222, 10000, 12345.67)
def main():
	module, exercise, i, j, k = kata
	print(f'module_{module:02}, ex_{exercise:02} : {i:.2f}, {j:.2e}, {k:.2e}')
main()