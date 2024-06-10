kata = (2019, 9, 25, 3, 30)

def main():
	year, month, day, hour, minute  = kata
	print(f'{month:02}/{day:02}/{year:02} {hour:02}:{minute:02}')
main()