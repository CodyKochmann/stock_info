def load_pickle(file_path):
	''' cleanly loads a pickle file '''
	from pickle import load
	return(load(open(file_path,'wb')))

