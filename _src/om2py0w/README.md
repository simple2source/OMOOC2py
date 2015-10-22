# OMOOC.py _ow周任务代码试作

## 0w 目标
### 实现小型记事本系统
- **功能**
 + 一次接受输入一行日记
 + 保存为本地文件
 + 再次运行系统时，能打印过往所有日记

- **思路**
 + 判断文件是否存在，如果存在则打印文件，否则新建文件并交互持续输出
 + 当交互界面输入exit的时候退出，并将输入的内容保存到新建的文件当中，输入的文件要换行的方式显示（此处用+\n来输入的文本换行）
 
- **代码**
```#/usr/bin/python
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
            f.close()```

- **反思**
- 
- CLI:
    + 交互
