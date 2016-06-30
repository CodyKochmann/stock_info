from replace_all import *

def last_char(in_txt):
	''' returns last nonspace char '''
	if '\t' in in_txt:
		in_txt=replace_all(in_txt,'\t','  ')
	while ' ' == in_txt[-1]:
		in_txt=in_txt[:-1]
	return(in_txt[-1])
