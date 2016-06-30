def save_pickle(file_path,data):
	''' cleanly saves a pickle file '''
	from pickle import dump
	dump(data,open(file_path,'wb'))

