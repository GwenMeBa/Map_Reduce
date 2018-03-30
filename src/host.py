#!/usr/bin/python
'''
Intervals sample
@author: Alejandro Lopez Mellina & Gwenaelle Mege Barriola
'''


from pyactor.context import set_context, create_host, Host, sleep, shutdown, sys
from pyactor.exceptions import TimeoutError


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


    def gestionCount(self, x):
        
        self.mapper.countWords(x, reducer)
        self.mapper1.countWords(x, reducer)
        self.mapper2.countWords(x, reducer) 
        
        return self.reducer.getCount()

    def gestionWord(self, x):

        self.mapper.wordCount(x, reducer)
        self.mapper1.wordCount(x, reducer)
        self.mapper2.wordCount(x, reducer)   
        
        return self.reducer.getWord()


class Mapper (object):
  _ask = {'countWords', 'wordCount'}
  _tell=['']
  _ref=['countWords', 'wordCount']
  
  def countWords(self, msg, reducer):
    lineas = open(msg, 'r').read() 
    li= ['*',';',',','.','-','$','!','"','%','&','/','(',')',':','=','?',']','+','<','>','{',']','^']
    for a in li:
      lineas=lineas.replace(a,'')
    reducer.reduceCount(len(lineas.split()))

  def wordCount(self, msg, reducer):
    file=open(msg,"r+")
    wordcount={}
    li= ['*',';',',','.','-','$','!','"','%','&','/','(',')',':','=','?',']','+','<','>','{',']','^']
    for a in li:
        file=file.replace(a,'')
    
    for word in file.read().split():
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

    def reduceCount(self, x):
        self.num_words=self.num_words+x

    def getCount(self):
        return self.num_words

    def reduceWord(self, x):
        self.num_words=self.num_words+x

    def getWord(self):
        return self.num_words


if __name__ == "__main__":
    set_context()
    host = create_host('http://127.0.0.1:1679')

    server = host.spawn('server', 'host/Server')
    server.init_st(host)
    sleep(2)

    print server.gestionCount("demo.txt")
    print server.gestionWord("demo.txt")

    shutdown()