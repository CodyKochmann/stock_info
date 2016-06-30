# coding: utf-8
# by: Cody Kochmann
# brings javascript's setTimeout function to python!

def setTimeout(function,delay_ms,*args):
  from threading import Timer
  t = Timer(delay_ms/1000.0, function, tuple(args))
  t.start() 

if __name__ == '__main__':
	l=[4,3,2,1]
	
	def tester():
	  global l
	  for i in l:
	    print(i)
	
	setTimeout(tester,2000)
	
	print('this should print before tester runs, even though its already running :)')
