#!/usr/bin/python

text = open("TextFile2.txt", 'r').read()
text2 = open("TextFile3.txt", 'a')
text2.write(text)
text2.write(text)
text2.close()

