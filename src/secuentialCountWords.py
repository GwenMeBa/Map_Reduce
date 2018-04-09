#!/usr/bin/python

'''
Intervals sample
@author: Alejandro Lopez Mellina & Gwenaelle Mege Barriola
'''

#Secuential words count
import sys, timeit
from pyactor.context import set_context, create_host, sleep, shutdown

if len(sys.argv) != 2:
  print 'Debe pasar un archivo'
else: 
  start = timeit.default_timer()
  lineas = open(sys.argv[1], 'r').read()
  li= ['*',';',',','.','-','$','!','"','%','&','/','(',')',':','=','?',']','+','<','>','{',']','^']
  for a in li:
    lineas=lineas.replace(a,'')
  
  print len(lineas.split())
  print timeit.default_timer() - start

  
  
