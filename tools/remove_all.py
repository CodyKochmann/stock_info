def remove_all(input_string,to_be_removed):
	''' removes all instance of a substring from a string '''
	while(to_be_removed in input_string):
		input_string = ''.join(input_string.split(to_be_removed))
	return(input_string)

if __name__ == '__main__':
	print(remove_all('hello world','l'))
