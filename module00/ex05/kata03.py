kata =  "The right format"

def main():
	j = 0
	len_kata = len(kata)
	while len_kata < 42:
		print('-', end="")
		j += 1
		len_kata += 1
	i = 0
	while (j < 42):
		print(kata[i], end="")
		i += 1
		j += 1
main()