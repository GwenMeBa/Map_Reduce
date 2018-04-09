#!/usr/bin/python utf-8
'''
Intervals sample
@author: Alejandro Lopez Mellina & Gwenaelle Mege Barriola
'''


from pyactor.context import set_context, create_host, Host, sleep, shutdown, sys, serve_forever
from pyactor.exceptions import TimeoutError
import collections, os, datetime, timeit, time

class Server(object):
    _ask = {'parsefile'}
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

    def parsefile(self, file, nmapper, nMappers):
        ca=open(file, 'r').readlines()
        
        ca1 = open(file+str(nmapper), 'w')

        if(nmapper==0): 
            ca1.write(str(ca[0:(len(ca)/3)]))
        if(nmapper==1): 
            ca1.write(str(ca[(len(ca)/3):2*(len(ca)/3)]))
        if(nmapper==2): 
            ca1.write(str(ca[2*(len(ca)/3):(len(ca))]))
        ca1.close()

    def gestionCount(self, x):

        for i in range(0,3):
            self.parsefile(x,i,3)
        start = timeit.default_timer()
        self.mapper.countWords(x,0, self.reducer, start)
        self.mapper1.countWords(x,1, self.reducer, start)
        self.mapper2.countWords(x,2, self.reducer, start) 

    def gestionWord(self, x):
        for i in range(0,3):
            self.parsefile(x,i,3)
        start = time.time()
        self.mapper.wordCount(x, 0, self.reducer, start)
        self.mapper1.wordCount(x, 1, self.reducer, start)
        self.mapper2.wordCount(x, 2, self.reducer, start) 
        


class Mapper (object):
  _ask = {''}
  _tell=['countWords', 'wordCount']
  _ref=['countWords', 'wordCount']
  
  def countWords(self, file, idmap, reducer,start):
    ca=open(file+str(idmap), 'r').read()
    li= ['*',';',',','.','-','$','!','"','%','&','/','\\','(',')',':','=','?',']','+','<','>','{','[','^']
    for a in li:
        ca=ca.replace(a, '')
    reducer.reduceCount(len(ca.split()), start)

  def wordCount(self, file, idmap, reducer, start):
    ca=open(file+str(idmap), 'r').read()
    li= ['*',';',',','.','-','$','!','"','%','&','/','\\','(',')',':','=','?',']','+','<','>','{','[','^','\\n']
    for a in li:
        ca=ca.replace(a, '')
    reducer.reduceWord(collections.Counter(map(str.lower,ca.split(' '))), start)

class Reducer (object):
    _ask = {''}
    _tell = [ 'reduceCount','reduceWord', 'getCount', 'getWord']

    def __init__(self):
        self.num_words = 0
        self.count=collections.Counter()
        self.mappersC= 3
        self.mappersW= 3

    def reduceCount(self, x, start):
        self.mappersC= self.mappersC-1
        self.num_words=self.num_words+x
        if (self.mappersC==0):
            val= (time.time() - start)
            print self.num_words
            print val 

    def reduceWord(self, x, start):
        self.mappersW= self.mappersW -1
        self.count=self.count+collections.Counter(x)
        if (self.mappersW==0):
            val= (time.time() - start)
            print dict(self.count)
            print val


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