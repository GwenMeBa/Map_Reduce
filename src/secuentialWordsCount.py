#!/usr/bin/python

'''
Intervals sample
@author: Alejandro Lopez Mellina & Gwenaelle Mege Barriola
'''

#Secuential count words
import sys
from pyactor.context import set_context, create_host, sleep, shutdown

if len(sys.argv) != 2:
	print 'Debe pasar un archivo'
else:
	file=open(sys.argv[1],"r+")
	wordcount={}
	li= ['*',';',',','.','-','$','!','"','%','&','/','(',')',':','=','?',']','+','<','>','{',']','^']
	for a in li:
		file=file.replace(a,'')
	
	for word in file.read().split():
    		if word not in wordcount:
        		wordcount[word] = 1
    		else:
        		wordcount[word] += 1
	print (word,wordcount)
	file.close();
