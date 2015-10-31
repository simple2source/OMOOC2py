#!/usr/bin/env python
#coding-utf-8
import sys,os
from sys import argv
script,filename = argv
if os.path.exists(filename):
    f = open(filename,'r')
    print f.read()
    while True:
        text = raw_input('pls input somethig :>')
        if text == 'exit':
            break
        else:
            f = open(filename,'a+')
            f.write(text+'\n')
else:
    while True:
        text = raw_input('pls input somehing :>')
        if text == 'exit':
            break
        else:
            #text = raw_input('pls input something >>:')
            f = open(filename,'a+')
            f.write(text+'\n')
