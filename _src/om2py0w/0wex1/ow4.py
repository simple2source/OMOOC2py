#/usr/bin/python
#coding=utf-8
import sys,os
from sys import argv
script,filename = argv
if os.path.exists(filename):
    f = open(filename,'r')
    print f.read()
else:
    while True:
        text = raw_input('pls input somehing :>')
        if text == 'exit':
            break
        else:
            #text = raw_input('pls input something >>:')
            f = open(filename,'a+')
            f.write(text+'\n')
            f.close()
