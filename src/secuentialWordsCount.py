#!/usr/bin/python

'''
Intervals sample
@author: Alejandro Lopez Mellina & Gwenaelle Mege Barriola
'''

#Secuential count words
import sys, timeit
from pyactor.context import set_context, create_host, sleep, shutdown

if len(sys.argv) != 2:
	print 'Debe pasar un archivo'
else:
	start = timeit.default_timer()
	with open(sys.argv[1],"r") as file:
		fi=file.read()
		print fi
		wordcount={}
		li= ['*',';',',','.','-','$','!','"','%','&','/','(',')',':','=','?',']','+','<','>','{',']','^']
		for a in li:
			fi=fi.replace(a,'')
		print fi
		for word in fi.split():
			if word not in wordcount:
				wordcount[word] = 1
			else:
				wordcount[word] += 1
		print wordcount
		print timeit.default_timer() - start
