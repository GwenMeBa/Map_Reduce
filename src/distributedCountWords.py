#!/usr/bin/python
'''
Intervals sample
@author: Alejandro Lopez Mellina & Gwenaelle Mege Barriola
'''
from pyactor.context import set_context, create_host, sleep, shutdown, interval, later
import sys



class Client (object):
	_tell = ['countWords','wordCounts']
	
	def countWords(self,msg):
		#hacer conteo de palabras en el mensaje
		#acceder al servidor http y conseguir el texto
		print len(msg.split())
	def wordsCount(self,msg):
		#hacer conteo de palabras en el mensaje
		pass


if __name__ == "__main__":

	if len(sys.argv) != 2:
		print 'Debe pasar un archivo'
	else:
		set_context()
		h = create_host()
		s1 = h.spawn('slave1', Client)
		s2 = h.spawn('slave2', Client)
		s3 = h.spawn('slave3', Client)
		lineas = open(sys.argv[1], 'r').read()
		li= ['*',';',',','.','-','$','!','"','%','&','/','(',')',':','=','?',']','+','<','>','{',']','^']
		for a in li:
			lineas=lineas.replace(a,'')
		lineas = lineas.split('\n')
		
		l=''
		for a in range(0,(len(lineas)/3)):
			l=l+' '+lineas[a]
		s1.countWords(l)
		l=''
		sleep(1)
		for a in range((len(lineas)/3),(2*(len(lineas)/3))):
			l=l+' '+lineas[a]
		s2.countWords(l)
		sleep(1)
		l=''
		for a in range(2*(len(lineas)/3),len(lineas)):
			l=l+' '+lineas[a]
		s3.countWords(l)
		sleep(1)
    		shutdown()



