import base64
import json
import pickle


class Base64():
	
	def write(self,myfile,data):
		Encodobj=base64.b64encode(data)
		try:
			fobj=open(myfile,'w')
			fobj.write(Encodobj)
			fobj.close()
		except IOError:
			print "Input File is not Exist"

	def read(self,myfile):
		try:
			fobj=open(myfile,'rb')
			data=fobj.read()
			orgData=base64.b64decode(data)
			fobj.close()
		except IOError:
			print "Input File is not exist"

		return orgData

class Mypickle():

	def write(self,myfile,data):
		try:
			fobj=open(myfile,'wb')
			pickle.dump(data,fobj)
			fobj.close()
		except IOError:
			print "input File is not Exist"

	def read(self,myfile):
		try:
			fobj=open(myfile,'rb')
			orgData=pickle.load(fobj)
			fobj.close()
			
		except IOError:
			print "input File is not Exist"
		
		return orgData
class Json():

	def write(self,myfile,data):
		try:
			fobj=open(myfile,'w')
			EncData=json.dumps(data)
			fobj.write(EncData)
			fobj.close()

		except IOError:
			print "input File is not Exist"

	def read(self,myfile):
		try:
			fobj=open(myfile,'r')
			data=fobj.read()
			orgData=json.loads(data)
			fobj.close()
		except IOError:
			print "Input File is not Exist"
		return orgData


'''test = Mypickle()
li=[1,2,3,4]
test.write('testfile.txt',li)
li2=test.read('testfile.txt')
print li2

if li==li2:
	print "correct"'''

'''test2 = Json()
ld=[3,4,5,6]
test2.write('test2.txt',ld)
ld2=test2.read('test2.txt')
print ld2

if ld==ld2:
	print "correct"'''

'''test=Base64()
li="tiru"
test.write('test111.dat',li)
print test.read('test111.dat')'''

