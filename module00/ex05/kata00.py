kata = (19,42,21)

def main():
	i = len(kata)
	if not len:
		print('Error')
		return
	print('The %d numbers are: ' % i, end="")
	while i > 1:
		print('%d, ' % kata[i - 1], end="")
		i -= 1
	print('%d' % kata[0])
main()