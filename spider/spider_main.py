#coding=utf-8
# Created by feizi at 2016/3/14

#spider entrance
import datetime

from spider import url_manager
from spider import html_downloader
from spider import html_parser
from spider import html_outputer

class SpiderMain(object):
    #构造器初始化
    def __init__(self):
        #url管理器
        self.urlManager = url_manager.UrlManager()
        #html下载器
        self.htmlDownloader = html_downloader.HtmlDownloader()
        #html解析器
        self.htmlParser = html_parser.HtmlParser()
        #页面渲染器
        self.htmlOutputer = html_outputer.HtmlOutputer()

    #爬虫调度器
    def crawl(self, url):
        #计数
        count = 1
        #将url添加进url管理器
        self.urlManager.add_new_url(url)

        #开始时间
        start_time = datetime.datetime.now()
        #循环爬取
        while self.urlManager.has_new_url():
            try:
                #1、获取待爬取的url
                new_url = self.urlManager.pop_new_url()
                print 'spider has started,at present, it craws %d : %s ' % (count, new_url)

                #2、下载html内容
                html_content = self.htmlDownloader.download(new_url)
                #3、解析html
                new_urls, new_datas = self.htmlParser.parse(new_url, html_content)
                #4、将新的url添加进url管理器，等待下一次爬取
                self.urlManager.add_new_urls(new_urls)
                #5、采集数据信息
                self.htmlOutputer.collect_data(new_datas)

                count = count + 1
            except Exception, e:
                print 'craw baidutieba information failed...Exception:', e

        end_time = datetime.datetime.now()
        print '总共耗时：%s 秒' % (end_time - start_time).seconds

        #6、最后将采集到的数据信息进行保存，（写文件或者数据库）
        # self.htmlOutputer.writeFile()
        self.htmlOutputer.insert()
if __name__ == '__main__':
    root_url = "http://tieba.baidu.com/p/4103105315"
    spider = SpiderMain()
    spider.crawl(root_url)