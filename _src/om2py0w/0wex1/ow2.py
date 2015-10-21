#coding=utf-8
import sys,os
if os.path.exists('456.txt'):
    a = open('456.txt','r')
    for b in a.readlines():
        print b
    a.close()
else:
    line = sys.stdin.readline()
    f = open('456.txt','a+')
    f.writelines(line)
    f.close()
    f = open('456.txt','r')
    for i in f.readlines():
        print i
