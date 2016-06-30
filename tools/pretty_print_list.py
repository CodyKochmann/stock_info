def pretty_print_list(li,seperator=''):
  while(len(li)):
    print(li.pop(0))
    print(seperator)
    
if __name__ == '__main__':
	l = 'hello world'.split(' ')
	pretty_print_list(l)

