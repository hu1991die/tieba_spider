#coding=utf-8
# Created by feizi at 2016/3/14
#url管理器
class UrlManager(object):
    #构造函数（定义待爬取的url集合和已爬取的url集合）
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    #添加一条待爬取的url
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            #该url既不在待爬取集合中也不在已爬取集合中，说明是一条新的url
            self.new_urls.add(url)

    #批量添加待爬取的url
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            #循环添加
            self.add_new_url(url)

    #判断是否还存在待爬取的url
    def has_new_url(self):
        return len(self.new_urls) > 0

    #获取一条待爬取的url
    def pop_new_url(self):
        #从待爬取集合中取出一条url
        new_url = self.new_urls.pop()
        #将该url添加进已爬取集合中
        self.old_urls.add(new_url)
        #返回一条待爬取的url
        return new_url