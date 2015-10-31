<<<<<<< HEAD
#!/usr/bin/env python
#coding-utf-8
=======
#!/usr/bin/python
#coding=utf-8
>>>>>>> 2a4ebccd1749ad8be2a88a6566910f95e03ca334
import sys,os
from sys import argv
script,filename = argv
if os.path.exists(filename):
    f = open(filename,'r')
    print f.read()
<<<<<<< HEAD
    while True:
        text = raw_input('pls input somethig :>')
        if text == 'exit':
            break
        else:
            f = open(filename,'a+')
            f.write(text+'\n')
=======
>>>>>>> 2a4ebccd1749ad8be2a88a6566910f95e03ca334
else:
    while True:
        text = raw_input('pls input somehing :>')
        if text == 'exit':
            break
        else:
            #text = raw_input('pls input something >>:')
            f = open(filename,'a+')
            f.write(text+'\n')
