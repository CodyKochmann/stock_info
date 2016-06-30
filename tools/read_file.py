def read_file(path):
	''' reads a file and returns it '''
	out=''
	try:
		with open(path,'r') as f:
			out = str(f.read())
	except:
		with open(path,'rb') as f:
			out = f.read()
	return(out)

if __name__ == '__main__':
	print(read_file(__file__))
