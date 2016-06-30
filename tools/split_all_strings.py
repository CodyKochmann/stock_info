def split_all_strings(input_array,splitter,keep_empty=False):
	out=[]
	while(len(input_array)):
		current=input_array.pop(0).split(splitter)
		while(len(current)):
			i=current.pop(0)
			if(len(i) or keep_empty):
				out.append(i)
	return(out)

if __name__ == '__main__':
	test = 'hello world or something like that'.split('l')
	#print('hello'.split('l')+'yolo'.split('o'))
	out = split_all_strings(test,'o')
	print(out)
	out = split_all_strings(out,' ')
	print(out)
