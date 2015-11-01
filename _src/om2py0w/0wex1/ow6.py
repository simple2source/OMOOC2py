#!/usr/bin/env python
#coding-utf-8
import sys,os
from sys import argv
script,filename = argv
m = 0
if os.path.exists(filename):
    f = open(filename,'r')
    #m = m+1
    #print m,f.readline()
    for i in f.readlines():
        m=m+1
        print m,'.',i
    print 'day now','\n'
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
