def zip_dir(zip_path, dir_name, v):
	''' zips a given directory '''
	from shutil import make_archive
	if v:
		print('zipping: %s'%(dir_name))
	make_archive(zip_path, 'zip', dir_name)

