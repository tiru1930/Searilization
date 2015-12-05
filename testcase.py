import unittest
from searilization import Json,Mypickle,Base64

class SamplInputs(unittest.TestCase):

	def test_case1(self):
		Data=[1,2,3,4]
		test=Mypickle()
		test.write('test.txt',Data)
		Out=test.read('test.txt')
		self.assertEqual(Data,Out)

	def test_case2(self):
		Data={1:'Hi',2:(2,3)}
		test=Mypickle()
		test.write('test.txt',Data)
		Out=test.read('test.txt')
		self.assertEqual(Data,Out)

	'''def test_case3(self):
		Data="Hello World"
		test=Json()
		test.write('test.txt',Data)
		Out=test.read('test.txt')
		self.assertEqual(Data,Out)'''

	def test_cas4(self):
		Data="Hi Good morning"
		test=Base64()
		test.write('test.txt',Data)
		Out=test.read('test.txt')
		self.assertEqual(Data,Out)

#if __name__ ==' __main__':
unittest.main()
	
