def lines(txt,allow_blank=True):
	''' cleanly splits lines to a list '''
	out=(txt.split('\n'))
	if allow_blank == False:
		new_out=[]
		for i in out:
			if len(i):
				new_out.append(i)
		out=new_out
	return(out)
