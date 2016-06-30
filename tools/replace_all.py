def replace_all(input_string,old,replacement):
	''' replaces every instance of old with replacement '''
	if old in replacement: # only do once if the replacement is in the target
		input_string = replacement.join(input_string.split(old))
	else:
		while(old in input_string):
			input_string = replacement.join(input_string.split(old))
	return(input_string)

if __name__ == '__main__':
	print(replace_all('hello world','l','i'))
