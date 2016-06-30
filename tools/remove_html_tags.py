from get_str_between import *

def remove_html_tags(input_text):
	return(' '.join(get_str_between(input_text,'>','<')))
