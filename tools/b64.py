
import base64

class b64():
	def e(input_str):
		'''b64 encodes an object'''
		return(base64.b64encode(input_str.encode('utf-8')))
	def d(input_str):
		'''b64 encodes an object'''
		return(base64.b64decode(input_str.decode('utf-8')))
	def test(input_str):
		'''tests to see if the string is b64 encoded'''
		print('Error: b64.test() is not ready')
		return()
		try:
			t=self.d(input_str)
			return(True)
		except:
			pass
		return(False)

if __name__ == '__main__':
	test = 'hello world'
	print(b64.test(test))
	test = b64.e(test)
	print(b64.test(test))
	print(test)
	test=b64.d(test)
	print(test)
