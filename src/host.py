#!/usr/bin/python utf-8
'''
Intervals sample
@author: Alejandro Lopez Mellina & Gwenaelle Mege Barriola
'''


from pyactor.context import set_context, create_host, Host, sleep, shutdown, sys, serve_forever
from pyactor.exceptions import TimeoutError
import collections, os, datetime, timeit

start = timeit.default_timer()
class Server(object):
    _ask = {''}
    _tell = ['init_st', 'gestionCount', 'gestionWord']
    _ref = ['gestionCount', 'gestionWord', 'init_st']

    def init_st(self, host):
       
        remote_host = host.lookup_url('http://127.0.0.1:1277/', Host)
        remote_host1 = host.lookup_url('http://127.0.0.1:1278/', Host)
        remote_host2 = host.lookup_url('http://127.0.0.1:1279/', Host)
        
        self.mapper = remote_host.spawn('mapper','host/Mapper') 
        self.mapper1 = remote_host1.spawn('mapper1','host/Mapper')    
        self.mapper2 = remote_host2.spawn('mapper2','host/Mapper')  
        self.reducer = host.spawn('reducer', 'host/Reducer')  
        print 'se han inicializado todos los mappers y el reducer'

    def gestionCount(self, x):
        
        ca=open(x, 'r').read().replace('\n', ' %')

        li= ['*',';',',','.','-','$','!','"','%','&','/','\\','(',')',':','=','?',']','+','<','>','{',']','^']
        for a in li:
            ca=ca.replace(a, '')
        ca=ca.split()
        
        start = timeit.default_timer()
        self.mapper.countWords(ca[0:(len(ca)/3)], self.reducer)
        print 'caca'
        self.mapper1.countWords(ca[(len(ca)/3):2*(len(ca)/3)], self.reducer)
        print 'asd'
        self.mapper2.countWords(ca[2*(len(ca)/3):(len(ca))], self.reducer) 

    def gestionWord(self, x):

        ca=open(x, 'r').read()
        
        li= ['*',';',',','.','-','$','!','"','%','&','/','\\','(',')',':','=','?',']','+','<','>','{','[','^']
        for a in li:
            ca=ca.replace(a, '')
        ca=ca.split()
        start = timeit.default_timer()
        self.mapper.wordCount(ca[0:(len(ca)/3)], self.reducer)
        self.mapper1.wordCount(ca[(len(ca)/3):2*(len(ca)/3)], self.reducer)
        self.mapper2.wordCount(ca[2*(len(ca)/3):(len(ca))], self.reducer) 
        


class Mapper (object):
  _ask = {''}
  _tell=['countWords', 'wordCount']
  _ref=['countWords', 'wordCount']
  
  def countWords(self, lineas, reducer):
    reducer.reduceCount(len(lineas))

  def wordCount(self, fi, reducer):      
    reducer.reduceWord(collections.Counter(map(str.lower,fi)))

class Reducer (object):
    _ask = {''}
    _tell = [ 'reduceCount','reduceWord', 'getCount', 'getWord']

    def __init__(self):
        self.num_words = 0
        self.count=collections.Counter()
        self.mappersC= 3
        self.mappersW= 3

    def reduceCount(self, x):
        self.mappersC= self.mappersC-1
        self.num_words=self.num_words+x
        if (self.mappersC==0):
            print timeit.default_timer() - start
            print self.num_words


    def reduceWord(self, x):
        self.mappersW= self.mappersW -1
        self.count=self.count+collections.Counter(x)
        if (self.mappersW==0):
            print timeit.default_timer() - start
            print dict(self.count)


if __name__ == "__main__":
    set_context()
    host = create_host('http://127.0.0.1:1679')

    server = host.spawn('server', 'host/Server')
    server.init_st(host)


    demo=raw_input('Escoge nombre de archivo:')
    os.system("cd ../src \n ./download "+demo)
    op=raw_input('Escoge opcion: \n 1. CountWord\n 2. WordCount')
    if op=='1':
        server.gestionCount("../src/"+demo)
    elif op=='2':
        server.gestionWord("../src/"+demo)
    else:
        print 'Opcion no correcta'

    serve_forever()
   # shutdown()