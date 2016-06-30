def write_file(path,data,binary=False):
	mode = 'w'
	if binary:
		mode+='b'
	with open(path,mode) as f:
		f.write(data)
