from replace_all import replace_all

def remove_useless_spaces(txt):
	txt = replace_all(txt,'  ',' ')
	if len(txt):
		if txt[0] == ' ':
			txt=txt[1:]
	if len(txt):
		if txt[-1] == ' ':
			txt=txt[:-1]
	return(txt)
