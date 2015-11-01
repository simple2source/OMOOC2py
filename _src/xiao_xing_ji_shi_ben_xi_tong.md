# 第一周：小型记事本系统

## 1、目标
#### 记事本系统实现写入、新建、清空

## 2、过程
#### 一、功能
+ 一次接受输入一行日记
+ 保存为本地文件
+ 再次运行系统时，能打印过往所有日记

#### 二、思路
+ 判断文件是否存在，如果存在则打印文件，否则新建文件并交互持续输出
+ 当交互界面输入exit的时候退出，并将输入的内容保存到新建的文件当中，输入的文件要换行的方式显示（此处用+\n来输入的文本换行）

#### 三、代码
```
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
            f.write(text+'\n')```
        
#### 四、反思
+ 没有实现代码交互传递参数来选择对应的操作，比如输入-c创建自己定义的文件，输入-h对此记事本系统的使用帮助等等

#### 五、重构
+ 小幅度修改，增加打印出文本行数，并且查看的时候可以继续输入追加文本内容
'''
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
'''
