# 0.1 GIt与Gitbook关联

## 目标
- **github仓库、gitbook分别更新文件，之间都能同步,实现互动**
 
## 背景
- **github账号已注册，用此账号登陆gitbook两者之间实现关联**

##配置
-  **1. 点击gitbook页面+新建book的时候注意，不要选择右边选项去导入账号**


- **2. 右上头像选项accout setting中进入页面后，选择ADD github，实现账号关联**

- **3.在accout setting中change passwd，此处前面由于用的github账号登陆，没有更新过密码，使用过程中一直无法验证，后面将这里的密码修改为github一样的密码，则可以正常连接，原因可能是用github登陆的时候，gitbook并没有密码**

- **4.书本建好之后，进入书本主页面，右下角有一个setting选项可以设置书本的基本信息，最下面有一个github选项点进去后在最下面设置 +add webhook,增加一个钩子，这里钩子作用是关联到github实现同步**

- **5.注意！尽量不要使用export github，使用过程中发现，第一次可以同步，而在后面的过程中同步不过来。使用export github ,gitbook的链接是：https://www.gitbook.com/simple2source 类的域名，使用add webhook后域名变化为：https://simple2source.gitbooks.io/ompy2/ 类域名，前一种类，测试发现是无法添加disqus插件的！**

- **6.在gitbook上假如已经设置add webhook，将add webhook链接复制下来，进入github，选择你新建的book已经关联的repository,进入到github的与gitbook关联的repository，选择右边的setting，在Webhooks&service里面添加刚刚复制的gitbook里面的链接**


