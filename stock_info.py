# coding: utf-8

from load_tools import *

def is_numeric(txt):
	'''confirms that the text is numeric'''
	out=len(txt)
	allowed_chars='0123456789-$%+.'
	allowed_last_char='1234567890%'
	for c in txt:
		if c not in allowed_chars:
			out=False
	if out and txt[-1] not in allowed_last_char:
		out=False
	return(out)

def stock_info(symbol):
	''' generates json data on the given stock from finviz.com '''
	html = get('http://finviz.com/quote.ashx?t=%s&ty=l&ta=0&p=d&b=1'%(symbol))
	
	# html = read_file('finviz.txt')
	
	html=(remove_html_tags(html))
	html=replace_all(html,'  ','\n')
	html=replace_all(html,'\\n','\n')
	html=replace_all(html,'\\r','\n')
	html=replace_all(html,'\n\n','\n')
	
	new_html = []
	for i in lines(html):
		new_html.append(remove_useless_spaces(i))
	html=new_html
	
	collected_values={}
	for i in range(len(html)):
		if is_numeric(html[i]) and len(html[i+1])<20:
			collected_values[html[i+1]]=html[i]
	
	return(collected_values)
	
if __name__ == '__main__':
	print(prettyfy(stock_info('LPTN')))
	
