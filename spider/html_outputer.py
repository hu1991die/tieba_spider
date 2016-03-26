#coding=utf-8
# Created by feizi at 2016/3/14
#html渲染器
import sys
from pymongo import MongoClient

reload(sys)
sys.setdefaultencoding('utf8')
class HtmlOutputer(object):
    #构造函数
    def __init__(self):
        self.datas = []

    #采集数据
    def collect_data(self, new_datas):
        if new_datas is None:
            return
        self.datas.append(new_datas)

    def insert(self):
        #创建链接
        client = MongoClient('127.0.0.1', 27017)

        #选择tieba数据库
        db = client.tieba

        #使用datas集合
        my_page_data = db.page_datas
        my_post_data = db.post_datas

        try:
            page = 1
            floor = 1
            for data in self.datas:
                print '========================================================当前贴吧第%d页数据===================================================\n\n' % page
                for i in range(len(data)):
                    page_data = {
                        "post_name": data[i]['post_name'].decode('UTF-8'),
                        "total_page":data[i]['total_page'].decode('UTF-8'),
                        "total_count":data[i]['total_count'].decode('UTF-8')
                    }
                    my_page_data.insert(page_data)

                    for card in data[i]['cards']:
                        print '------------------------------------------当前贴吧第%d楼--------------------------------------------\n\n' % floor
                        post_data = {
                            "user_name":card['user_name'].decode('UTF-8'),
                            "head_photo":card['head_photo'].decode('UTF-8'),
                            "user_title":card['user_title'].decode('UTF-8'),
                            "user_level":card['user_level'].decode('UTF-8'),
                            "post_content":card['post_content'].decode('UTF-8'),
                            "post_floor":card['post_floor'],
                            "post_time":card['post_time'],
                            "post_terminal":card['post_terminal']
                        }
                        my_post_data.insert(post_data)
                        floor = floor + 1
                page = page + 1
        except Exception, e:
            print Exception,":",e


    #写文件
    def writeFile(self):
        f = file('tieba_spider.txt', 'w+')
        try:
            page = 1
            floor = 1
            for data in self.datas:
                f.writelines('========================================================当前贴吧第%d页数据===================================================\n\n' % page)
                for i in range(len(data)):
                    f.writelines('贴吧名称:%s \n' % (data[i]['post_name'].decode('UTF-8')))
                    f.writelines('总共页数:%s \n' % (data[i]['total_page'].decode('UTF-8')))
                    f.writelines('回复贴数:%s \n' % (data[i]['total_count'].decode('UTF-8')))

                    for card in data[i]['cards']:
                        f.writelines('------------------------------------------当前贴吧第%d楼--------------------------------------------\n\n' % floor)
                        f.writelines('吧友昵称:%s \n' % (card['user_name'].decode('UTF-8')))
                        f.writelines('吧友头像:%s \n' % (card['head_photo'].decode('UTF-8')))
                        f.writelines('吧友头衔:%s \n' % (card['user_title'].decode('UTF-8')))
                        f.writelines('吧友级别:%s \n' % (card['user_level'].decode('UTF-8')))
                        f.writelines('发帖内容:%s \n' % (card['post_content'].decode('UTF-8')))
                        f.writelines('第几楼:%s \n' % (card['post_floor']))
                        f.writelines('发贴时间:%s \n' % (card['post_time']))
                        f.writelines('来自客户端:%s \n' % (card['post_terminal']))
                        floor = floor + 1

                page = page + 1
        except Exception, e:
            print Exception,":",e
        f.close()