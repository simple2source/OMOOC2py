# 0.2 gitbook添加评论插件disqus
## 目标
- ** 实现gitbook上评论功能**

## 方法
- **注册disqus,https://disqus.com/ ，通过disqus插件生成专用的名字**

- **disqus注册后，点击右上add dis site，选择模版，自定义名字，名字要记住，这是作为专用名字写入到配置文件当中的**

## 配置
- **1、在Github对应的gitbook库中，新建一个book.json,配置文件如下：

- ** ```{
    "plugins": ["disqus"],
    "pluginsConfig": {
        "disqus": {
            "shortName": "XXXXXXX"
        }
    }  
}```**

- **官方参考链接**：https://github.com/GitbookIO/plugin-disqus

- **在网页版gitbook中页面编辑book，右上方有add plugin的选项，尝试添加了一个disqus插件，实质上就是生成了一个Book.json的文件，但是不知道为何评论功能没有展示出来？**

## 其他
- ** 现阶段都是通过网页版点击出来的，没有使用命令行**
- ** node.js 不懂**


