#!/usr/bin/python

'''
Intervals sample
@author: Alejandro Lopez Mellina & Gwenaelle Mege Barriola
'''

#Secuential words count
import sys
from pyactor.context import set_context, create_host, sleep, shutdown

if len(sys.argv) != 2:
	print 'Debe pasar un archivo'
else: 
	lineas = open(sys.argv[1], 'r').read()
	li= ['*',';',',','.','-','$','!','"','%','&','/','(',')',':','=','?',']','+','<','>','{',']','^']
	for a in li:
		lineas=lineas.replace(a,'')
	
	print len(lineas.split())
	
	
