import os,sys
from sys import argv
script,text = argv
#os.path.exists('123.txt'):
note = open('123.txt','a+')
note.writelines(text)
note.close()
note = open('123.txt','r')
line=note.readlines()
for item in line:
    print item
