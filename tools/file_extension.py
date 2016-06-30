def file_extension(input_path):
  return(input_path.split('.')[-1])
  
if __name__ == '__main__':
	print(file_extension(__file__))
