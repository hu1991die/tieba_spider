# 使用python+mongodb爬取百度贴吧的帖子

本项目主要使用了python语言来爬取百度贴吧的一些帖子，之后将爬取到的帖子数据保存到mongodb数据库中。

## python环境

这里，关于python环境的安装，具体步骤略，大伙儿自行百度即可，这里采用的版本环境主要为2.7.6。

![](http://i.imgur.com/4lnfVne.jpg)

## mongoDB数据库

MongoDB是一个介于关系数据库和非关系数据库之间的产品，是非关系数据库当中功能最丰富，最像关系数据库的。他支持的数据结构非常松散，是类似 json的bjson格式，因此可以存储比较复杂的数据类型。官方网站：[http://www.mongodb.org](http://www.mongodb.org "http://www.mongodb.org")

MongoDB提供了可用于32位和64位系统的预编译二进制包，你可以从MongoDB官网下载安装，MongoDB预编译二进制包下载地址：[http://www.mongodb.org/downloads](http://www.mongodb.org/downloads "http://www.mongodb.org/downloads")

根据你的系统下载 32 位或 64 位的 .msi 文件，下载后双击该文件，按操作提示安装即可。

具体安装教程可以参考：[MongoDB 菜鸟教程](http://www.runoob.com/mongodb/mongodb-window-install.html "http://www.runoob.com/mongodb/mongodb-window-install.html")

好了，虽然现在已经搭建好了python环境，也安装好了mongdb环境，但是要想在python中操作mongdb数据库，暂时还是不行的，还得需要最后一个步骤，即需要安装一个pymongo的类库，就和一个插件差不多。

安装mongo的python模块，可以到[http://pypi.python.org/pypi/pymongo/](http://pypi.python.org/pypi/pymongo/ "http://pypi.python.org/pypi/pymongo/")下载pymongo-1.9.win32-py2.7.exe然后直接运行，安装完成就可以开始编码了。

![](http://i.imgur.com/UrFIPTd.jpg)

爬取完帖子数据之后，保存在mongdb数据库中的效果：

![](http://i.imgur.com/pOUHXZz.jpg)


python爬虫程序运行的效果：

![](http://i.imgur.com/gFTaOPE.jpg)

因为目前只爬取了其中的某一个帖子：[Python吧水楼！](http://tieba.baidu.com/p/4103105315 "http://tieba.baidu.com/p/4103105315")

大家可以看到耗时总共40秒，效率上还是很慢的，而且这次也只是单线程去爬取，资源没有得到很充分的利用，效率慢暂且还是可以理解的，下次再慢慢进步，尝试一下多线程爬取的效果。敬请期待！！
