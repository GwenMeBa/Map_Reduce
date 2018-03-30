#!/usr/bin/python
'''
Intervals sample
@author: Alejandro Lopez Mellina & Gwenaelle Mege Barriola
'''
from pyactor.context import set_context, create_host, serve_forever


if __name__ == "__main__":
    set_context()
    host = create_host('http://127.0.0.1:1279/')

    print 'host listening at port 1279'

    serve_forever()