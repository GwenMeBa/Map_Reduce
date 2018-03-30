#!/usr/bin/python utf-8
'''
Intervals sample
@author: Alejandro Lopez Mellina & Gwenaelle Mege Barriola
'''


from pyactor.context import set_context, create_host, Host, sleep, shutdown, sys, serve_forever
from pyactor.exceptions import TimeoutError
import collections

class Server(object):
    _ask = {'gestionCount', 'gestionWord'}
    _tell = ['init_st']
    _ref = ['gestionCount', 'gestionWord', 'init_st']

    def init_st(self, host):
       
        remote_host = host.lookup_url('http://127.0.0.1:1277/', Host)
        print 'a'
        remote_host1 = host.lookup_url('http://127.0.0.1:1278/', Host)
        remote_host2 = host.lookup_url('http://127.0.0.1:1279/', Host)
        
        self.mapper = remote_host.spawn('mapper','host/Mapper') 
        self.mapper1 = remote_host1.spawn('mapper1','host/Mapper')    
        self.mapper2 = remote_host2.spawn('mapper2','host/Mapper')  
        print 'e'
        self.reducer = host.spawn('reducer', 'host/Reducer')  
        print 'i'

    def gestionCount(self, x):
        
        url=x[x.rfind('/')+1:]
        ca=open(url, 'r').read()
        ca=ca.split(' ')
        l=''
        for a in range(0,(len(ca)/3)):
            l=l+' '+ca[a]
        self.mapper.countWords(l, self.reducer)
        l=''
        sleep(1)
        for a in range((len(ca)/3),(2*(len(ca)/3))):
            l=l+' '+ca[a]
        self.mapper1.countWords(l, self.reducer)
        sleep(1)
        l=''
        for a in range(2*(len(ca)/3),len(ca)):
            l=l+' '+ca[a]
        self.mapper2.countWords(l, self.reducer) 

        return self.reducer.getCount()

    def gestionWord(self, x):

        url=x[x.rfind('/')+1:]
        ca=open(url, 'r').read()
        ca= ca.split(' ')
        l=''
        for a in range(0,(len(ca)/3)):
            l=l+' '+ca[a]
        self.mapper.wordCount(l, self.reducer)
        l=''
        sleep(1)
        for a in range((len(ca)/3),(2*(len(ca)/3))):
            l=l+' '+ca[a]
        self.mapper1.wordCount(l, self.reducer)
        sleep(1)
        l=''
        for a in range(2*(len(ca)/3),len(ca)):
            l=l+' '+ca[a]
        self.mapper2.wordCount(l, self.reducer) 
    
        
        return self.reducer.getWord()


class Mapper (object):
  _ask = {'countWords', 'wordCount'}
  _tell=['']
  _ref=['countWords', 'wordCount']
  
  def countWords(self, lineas, reducer):
    print lineas
    li= ['*',';',',','.','-','$','!','"','%','&','/','(',')',':','=','?',']','+','<','>','{',']','^']
    for a in li:
      lineas=lineas.replace(a,' ')
    reducer.reduceCount(len(lineas.split()))

  def wordCount(self, fi, reducer):
    print fi    
    wordcount={}
    li= ['*',';',',','.','-','$','!','"','%','&','/','(',')',':','=','?',']','+','<','>','{',']','^']
    for a in li:
        fi=fi.replace(a,' ')
        
    for word in fi.split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
        
    reducer.reduceWord(wordcount)

class Reducer (object):
    _ask = {'reduceCount','getCount', 'reduceWord', 'getWord'}
    _tell = [ '__init__']

    def __init__(self):
        self.num_words = 0
        self.words={}
        self.count=collections.Counter(self.words)

    def reduceCount(self, x):
        self.num_words=self.num_words+x

    def getCount(self):
        return self.num_words

    def reduceWord(self, x):
        self.count=self.count+collections.Counter(x)

    def getWord(self):
        return self.count


if __name__ == "__main__":
    set_context()
    host = create_host('http://127.0.0.1:1679')

    server = host.spawn('server', 'host/Server')
    server.init_st(host)


    demo=raw_input('Escoge nombre de archivo:')
    print server.gestionCount(demo)
    print server.gestionWord(demo)

    serve_forever()
   # shutdown()