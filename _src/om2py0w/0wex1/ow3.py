#/usr/bin/python
#coding=utf-8
import sys,os
from sys import argv
if os.path.exists('789.txt'):
    f = open('789.txt','r')
    print f.read()
else:
    while True:
        text = raw_input('pls input somehing :>')
        if text == 'exit':
            break
        else:
            #text = raw_input('pls input something >>:')
            f = open('789.txt','a+')
            f.write(text+'\n')
            f.close()
