# 0.3 Git基础使用

##1、目标
- window、Linux上实现git推送github

##2、步骤
- **window 上实现远程本地仓库同步**
 + 先安装Git客户端“TortoiseGit”，然后安装TortoiseGit的安装程序和语言包，此处有详细步骤，[git window安装](http://backlogtool.com/git-guide/cn/intro/intro2_1.html)
 + 安装完之后，点击在当前目录空白处右键，有git bash，可以向linux中一样通过命令行的方式来进行git push clone等等操作，另外还有图形的方式点击。
 + 如果用window git bash命令行，可以参考此处 [window下git仓库部署](http://blog.jobbole.com/78960/)，基本上和Linux中一样。

- **Linux上实现远程本地仓库同步**
  + 使用的是 Ubuntu 14.04.3 LTS \n \l ,redhat使用相差无几
  + 安装git 
  ```sudo apt-get install git```
  + 新建一个目录用来初始化仓库
  ```mkdir code,  
     cd code ,
     git init```
  + 配置全局变量，用来认证github账号信息,填写自己github账号和邮箱（网上许多教程缺少这一步骤）

``` git config --global user.email "expamle@126.com",
    git config --global user.name "simple2source" ```
  + Linux上要实现密钥认证github才能推送
   + 生成密钥，复制Github设置里面
   + 具体步骤 [见此处](http://www.cnblogs.com/plinx/archive/2013/04/08/3009159.html)
   + ssh git 测试能否连接上Github

- 在本地添加一个Origin的命名为远程github上存在的仓库
``` git remote add origin git@github.com:simple2source/xxx.git ```
    + touch a.txt 测试 git add a.txt ,git commit -m "version1.0"
    + git push origin master 报错：
    ```To https://github.com/simple2source/OMOOC2py.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/simple2source/OMOOC2py.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.```
  + 测试发现第一次是不能使用git push origin master 应该使用git pull origin master 来进行推送，这个pull，也代表从远程fetch到本地和提交到远程两种行为，据我理解可能是本地文件没有克隆远程仓库直接推送有安全限制，这里有完整讨论 [git push和pit pull两种行为](http://segmentfault.com/a/1190000002783245)
  + 这里收集部分 [git 报错](http://my.oschina.net/psuyun/blog/123005) ，使用过程还有许多报错，但是用Google基本轻松都解决了，也就不记录

## 3、Git使用资料收集
 + [廖雪峰git教程](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)
 + Git权威指南
 + 
  
