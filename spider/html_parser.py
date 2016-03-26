#coding=utf-8
# Created by feizi at 2016/3/14
import json
import re
import urlparse

from bs4 import BeautifulSoup
#html解析器
class HtmlParser(object):
    def has_datafield(self, tag):
        return tag.has_attr('data-field')

    #解析html
    def parse(self, page_url, html_content):
        if page_url is None or html_content is None:
            return

        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_datas = self._get_new_datas(page_url, soup)

        return new_urls, new_datas

    #获取页面中下一页的url链接
    def _get_new_urls(self, page_url, soup):
        #定义一个集合
        new_urls = set()
        page_num = soup.find('li', class_='l_reply_num').find_next("span").find_next_sibling().get_text()
        # page_num = 1

        if page_num > 0:
            for i in range(int(page_num) + 1):
                #http://tieba.baidu.com/p/4103105315?pn=1
                new_url = '?pn=' + str(i + 1)
                new_full_url = urlparse.urljoin(page_url, new_url)
                new_urls.add(new_full_url)
        return new_urls

    #爬取有效的数据
    def _get_new_datas(self, page_url, soup):
        #定义列表
        res_data = []

        #定义字典(贴吧数据)
        post_data = {}

        #贴吧名称
        post_name = soup.find('div', class_='core_title core_title_theme_bright').find_next('h1').get_text().strip()
        # print post_name

        span_node = soup.find('li', class_='l_reply_num').find_next("span")
        #总共页数
        total_page = span_node.get_text()
        # print total_page

        #回复贴
        total_count = span_node.find_next_sibling().get_text()
        # print total_count

        post_data['post_name'] = post_name
        post_data['total_page'] = total_page
        post_data['total_count'] = total_count

        #抓取每一页的楼层
        div_nodes = soup.find('div', class_='p_postlist').find_all('div', class_=re.compile(r'l_post j_l_postl _post_bright\s+\w+|\w*\s*'), recursive=False)
        if div_nodes is not None and len(div_nodes) > 0:
            #存放所有的贴列表
            cards = []

            #循环每一页的楼层
            for div_node in div_nodes:
                if(self.has_datafield(div_node) == False):
                     continue

                #帖子数据(每一页都会实例化一个新的字典，分配新的内存空间)
                card_data = {}

                #吧友昵称
                user_name = div_node.find('ul', class_='p_author').find_next('li', class_='d_name').find_next('a', attrs={'alog-group':'p_author'}).text.strip()
                # print user_name

                #吧友头像
                head_photo = div_node.find('div', class_='icon_relative j_user_card').find_next('a').find_next('img')['src'].strip()
                # print head_photo

                #吧友头衔
                user_title = div_node.find('div', class_='p_badge').find('div', class_=re.compile(r'd_badge_title\s*')).text.strip()
                # print user_title

                #吧友级别
                user_level = div_node.find('div', class_='p_badge').find_next('div', class_='d_badge_lv').text.strip()
                # print user_level

                #发帖内容
                post_content = div_node.find('cc').find_next('div').text.strip()
                # print post_content

                #抓取json字符串
                jsonStr = div_node['data-field']
                #解析json串
                datafield = json.loads(jsonStr)

                #第几楼
                post_floor = (str)(datafield['content']['post_no'])
                # print post_floor

                #发贴时间
                post_time = datafield['content']['date']
                # print post_time

                #来自客户端
                post_terminal = datafield['content']['open_type'].encode('UTF-8')
                # print post_terminal

                card_data['user_name'] = user_name
                card_data['head_photo'] = head_photo
                card_data['user_title'] = user_title
                card_data['user_level'] = user_level
                card_data['post_floor'] = post_floor
                card_data['post_terminal'] = post_terminal
                card_data['post_time'] = post_time
                card_data['post_content'] = post_content
                cards.append(card_data)

            post_data['cards'] = cards
        res_data.append(post_data)
        return res_data