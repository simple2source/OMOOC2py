# GUI界面记事本交互系统
## 1、需求：gui界面展示交互记事本

## 2、实现：Tkinter库

## 3、代码：

```#！/usr/bin/env python
''' 简陋的gui打印界面'''

import os,sys
from Tkinter import *
def print_log():       # 定义打印按钮函数
    if os.path.exists('myday.txt'):
        f = open('myday.txt','r')
        for i in f.readlines():
            print i
        print "input other or exit"
        while True:
            #print "input other or exit"
            text = raw_input('day,now:>>')
            if text == 'exit':
                break
            else:
               f = open('myday.txt','a+')
               f.write(text+'\n')
    else:
        print "input other or exit"
        while True:
            text = raw_input('day,now:>>')
            if text == 'exit':
                break
            else:
                
               f = open('myday.txt','a+')
               f.write(text+'\n')
        
win = Tk()               #  Tk的主窗口
win.title('Tkinter')


btn = Button(win,text='print',command=print_log)   #定义一个print 按钮
btn.pack(expand=YES,fill=BOTH)

mainloop()           #  窗口会一直显示```

## 4、重构：


