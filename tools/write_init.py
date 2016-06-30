import os
from time import sleep

sleep(0.5)

def file_name():
	return(__file__.split('/')[-1])

targets=os.listdir('./')

targets.remove(file_name())

# remove __init__.py
if('__init__.py' in targets):
	targets.remove('__init__.py')

# remove everything that isn't a python file
for i in list(targets):
	if('.py' != i[-3:]):
		targets.remove(i)

def to_pct(count,total):
	total=total*1.0
	count=count*1.0
	percent=int((count/total)*100)
	return(percent)

with open('./__init__.py','w') as f:
	f.write('# this file makes all functions in this directory available as a package.\n\n')
	count = len(targets)*1.0
	while(len(targets)):
		sleep(0.1)
		i = targets.pop(0)
		print('{:>3}% - {}'.format(
			to_pct((count-len(targets)),count), 
			i))
		f.write('from %s import *\n'%(i[:-3]))

print('')
print('Done!')
