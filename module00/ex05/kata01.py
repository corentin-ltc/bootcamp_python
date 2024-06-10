kata = {
	'Python': 'Guido van Rossum',
	'Ruby' : 'Yukihiro Matsumoto',
	'PHP': 'Rasmus Lerdorf',
}

def main():
	for language, creator in kata.items():
		print(f'{language} was created by {creator}')
main()