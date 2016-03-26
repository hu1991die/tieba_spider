# coding=utf-8
# Created by feizi at 2016/3/15
import json
import re

from bs4 import BeautifulSoup
from pymongo import MongoClient

html_doc = """
<div class="l_post j_l_post l_post_bright  " data-field="{&quot;author&quot;:{&quot;user_id&quot;:985654380,&quot;user_name&quot;:&quot;mituningwang&quot;,&quot;name_u&quot;:&quot;mituningwang&amp;ie=utf-8&quot;,&quot;user_sex&quot;:1,&quot;portrait&quot;:&quot;6ce46d6974756e696e6777616e67bf3a&quot;,&quot;is_like&quot;:1,&quot;level_id&quot;:10,&quot;level_name&quot;:&quot;\u63a2\u82b1&quot;,&quot;cur_score&quot;:2246,&quot;bawu&quot;:0,&quot;props&quot;:null},&quot;content&quot;:{&quot;post_id&quot;:77437990476,&quot;is_anonym&quot;:false,&quot;open_id&quot;:&quot;tbclient&quot;,&quot;open_type&quot;:&quot;android&quot;,&quot;date&quot;:&quot;2015-10-15 17:49&quot;,&quot;vote_crypt&quot;:&quot;&quot;,&quot;post_no&quot;:2,&quot;type&quot;:&quot;0&quot;,&quot;comment_num&quot;:1,&quot;ptype&quot;:&quot;0&quot;,&quot;is_saveface&quot;:false,&quot;props&quot;:null,&quot;post_index&quot;:1,&quot;pb_tpoint&quot;:null}}">            <div class="user-hide-post-position"></div><div class="d_author">    			<ul class="p_author">
				<li class="icon">
		  			<div class="icon_relative j_user_card" data-field="{&quot;un&quot;:&quot;mituningwang&quot;}">
				  		<a style="" target="_blank" class="p_author_face " href="/home/main?un=mituningwang&amp;ie=utf-8&amp;fr=pb&amp;ie=utf-8"><img username="mituningwang" class="" src="http://tb.himg.baidu.com/sys/portrait/item/6ce46d6974756e696e6777616e67bf3a"></a>

			  		</div>
			 	</li>
			 	<li class="d_nameplate">

				</li>
			 	<li class="d_name" data-field="{&quot;user_id&quot;:985654380}">

				 	<a data-field="{&quot;un&quot;:&quot;mituningwang&quot;}" alog-group="p_author" title="该用户已经连续签到108天了，连续30天一举“橙”名" class="p_author_name sign_highlight j_user_card" href="/home/main?un=mituningwang&amp;ie=utf-8&amp;fr=pb&amp;ie=utf-8" target="_blank">mituningwang</a>
			 	</li>
			 				<li class="d_icons">
	 			<div class="icon_wrap  icon_wrap_theme1 d_pb_icons "><a style="background: url(http://tb1.bdstatic.com/tb/cms/com/icon/104_14.png?stamp=1458014095) no-repeat -4800px  0;top:0px;left:0px" data-slot="1" data-name="signprize" data-field="{&quot;name&quot;:&quot;signprize&quot;,&quot;end_time&quot;:&quot;1458316800&quot;,&quot;category_id&quot;:104,&quot;slot_no&quot;:&quot;1&quot;,&quot;title&quot;:&quot;\u9ad8\u7ea7\u6838\u5fc3\u7528\u6237&quot;,&quot;intro&quot;:&quot;\u624b\u673a\u7aef\u8fde\u7eed\u7b7e\u523090\u5929\u53ef\u83b7\u5f97\u672c\u5370\u8bb0&quot;,&quot;intro_url&quot;:&quot;http:\/\/tieba.baidu.com\/mo\/q\/medal&quot;,&quot;price&quot;:0,&quot;value&quot;:&quot;3&quot;,&quot;sprite&quot;:{&quot;1&quot;:&quot;1458014095,94&quot;,&quot;2&quot;:&quot;1458014095,95&quot;,&quot;3&quot;:&quot;1458014095,96&quot;}}" target="_blank" href="http://tieba.baidu.com/mo/q/medal" class="j_icon_slot" title="高级核心用户" locate="signprize_3#icon">  <div class=" j_icon_slot_refresh"></div></a></div>

			</li>
			 	<li class="l_badge" style="display:block;">
			 		<div class="p_badge">
			 			<a href="/f/like/level?kw=python&amp;ie=utf-8&amp;lv_t=lv_nav_intro" target="_blank" class="user_badge d_badge_bright d_badge_icon3" title="本吧头衔10级，经验值2246，点击进入等级头衔说明页"><div class="d_badge_title ">探花</div><div class="d_badge_lv">10</div></a>
			 		</div>
			 	</li>
			</ul></div><div class="d_post_content_main">    <div class="p_content p_content_icon_row1 p_content_nameplate"><div class="save_face_bg_hidden save_face_bg_0"><a class="save_face_card"></a>            </div>        <cc><div id="post_content_77437990476" class="d_post_content j_d_post_content  clearfix">            哇，剽窃我的创意<img class="BDE_Smiley" width="30" height="30" changedsize="false" src="http://static.tieba.baidu.com/tb/editor/images/client/image_emoticon25.png"></div><br></cc><br><div class="user-hide-post-down" style="display: none;"></div>        <div class="achievement_medal_section"></div></div>    <div class="core_reply j_lzl_wrapper"><div class="core_reply_tail "><div class="j_lzl_r p_reply" data-field="{'pid':'77437990476','total_num':'1'}"><a href="#" class="lzl_link_unfold" style="display:none;">回复(1)</a><span class="lzl_link_fold" style="display:">收起回复</span></div><ul class="p_tail"><li><span>2楼</span></li><li><span>2015-10-15 17:49</span></li></ul><ul class="p_mtail"><li class="j_jb_ele"><a href="#" onclick="window.open('http://tieba.baidu.com/complaint/info?type=0&amp;cid=0&amp;tid=4103105315&amp;pid=77437990476','newwindow', 'height=900, width=800, toolbar =no, menubar=no, scrollbars=yes, resizable=yes, location=no, status=no');return false;" class="complaint complaint-opened" data-checkun="un">举报</a>&nbsp;|<span class="super_jubao"><a href="#" onclick="window.open('http://tieba.baidu.com/complaint/info?type=1&amp;cid=0&amp;tid=4103105315&amp;pid=77437990476','newwindow', 'height=900, width=800, toolbar =no, menubar=no, scrollbars=yes, resizable=yes, location=no, status=no');return false;">个人企业举报</a><a href="#" onclick="window.open('http://tieba.baidu.com/complaint/info?type=2&amp;cid=0&amp;tid=4103105315&amp;pid=77437990476','newwindow', 'height=900, width=800, toolbar =no, menubar=no, scrollbars=yes, resizable=yes, location=no, status=no');return false;">垃圾信息举报</a></span></li><li><span class="p_tail_txt">来自</span><span class="tip_bubble_con"></span><a data-tip="超萌态动画表情来袭，速度抢先体验！" class="p_tail_wap" href="http://c.tieba.baidu.com/c/s/download/pc?src=webtbGF" target="_blank">Android客户端</a></li></ul><ul class="p_props_tail props_appraise_wrap"></ul></div><div class="j_lzl_container core_reply_wrapper" data-field="{'pid':'77437990476','floor_num':'2'}" style="display:"><div class="core_reply_border_top"></div><div class="j_lzl_c_b_a core_reply_content"><ul class="j_lzl_m_w" style="display:"><li class="lzl_single_post j_lzl_s_p first_no_border" data-field="{'pid':'77437990476','spid':'77438024492','user_name':'吃猫丶的鱼','portrait':'5235e59083e78cabe4b8b6e79a84e9b1bc2220'}"><a data-field="{'un':'吃猫丶的鱼'}" target="_blank" class="j_user_card lzl_p_p" href="/home/main?un=%E5%90%83%E7%8C%AB%E4%B8%B6%E7%9A%84%E9%B1%BC&amp;ie=utf-8&amp;fr=pb" username="吃猫丶的鱼"><img src="http://tb.himg.baidu.com/sys/portrait/item/5235e59083e78cabe4b8b6e79a84e9b1bc2220"></a><div class="lzl_cnt"><a class="at j_user_card " data-field="{'un':'吃猫丶的鱼'}" alog-group="p_author" target="_blank" href="/home/main?un=%E5%90%83%E7%8C%AB%E4%B8%B6%E7%9A%84%E9%B1%BC&amp;ie=utf-8&amp;fr=pb" username="吃猫丶的鱼">吃猫丶的鱼</a>:&nbsp;<span class="lzl_content_main">Who are you?<img class="BDE_Smiley" width="30" height="30" changedsize="false" src="http://static.tieba.baidu.com/tb/editor/images/client/image_emoticon15.png"></span><div class="lzl_content_reply"><span class="lzl_jb" style="display:none"><a href="#" data-field="{'delete_mine':'0','user_name':'吃猫丶的鱼'}" class="lzl_jb_in">举报</a>&nbsp;|&nbsp;</span><span class="lzl_op_list j_lzl_o_l"></span><span class="lzl_time">2015-10-15&nbsp;17:50</span><a href="#" class="lzl_s_r">回复</a></div></div></li><li class="lzl_li_pager j_lzl_l_p lzl_li_pager_s" data-field="{total_num:1,total_page:1}"><a class="j_lzl_p btn-sub btn-small pull-right" href="##"><i class="icon-reply"></i>我也说一句</a><p>&nbsp;</p></li></ul><div class="lzl_editor_container j_lzl_e_c lzl_editor_container_s" style="display:none;"></div><input type="text" class="j_lzl_e_f_h" style="display:none;"></div><div class="core_reply_border_bottom"></div></div></div></div><div class="clear"></div></div>
"""

# soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')
# print (soup.prettify())

# count = soup.find('li', class_='l_reply_num').find_next("span").find_next_sibling().get_text()
# if count > 0:
#     for i in range(int(count) + 1):
#         new_url = '?pn=' + str(i)
# print new_url

# div_nodes = soup.find_all('div', class_='l_post j_l_post l_post_bright  ')
# count = 1
# for div in div_nodes:
#     print div
#     count = count + 1
# print count

# post_name = soup.find('div', class_='core_title core_title_theme_bright').find_next('h1').get_text()
# print post_name.strip()

# user_name = soup.find('ul', class_='p_author').find_next('li', class_='d_name').find_next('a').text
# # user_name = soup.find('div', class_='icon_relative j_user_card').find_next('a').find_next('img')['username']
# print user_name.strip()
# #
# head_photo = soup.find('div', class_='icon_relative j_user_card').find_next('a').find_next('img')['src']
# print head_photo.strip()
# #
# user_title = soup.find('div', class_='p_badge').find('div', class_=re.compile(r'd_badge_title\s*')).text
# print user_title.strip()
# #
# user_level = soup.find('div', class_='p_badge').find_next('div', class_='d_badge_lv').text
# print user_level.strip()
#
# post_floor = soup.find('div', class_='d_post_content_main').find('div', class_='core_reply j_lzl_wrapper').find('div', class_='core_reply_tail ').li.text
# print post_floor
#
# post_terminal = soup.find('ul', class_='p_mtail').find('a', class_='p_tail_wap').text
# print post_terminal.strip()
# #
# post_time = soup.find('div', class_='core_reply_tail ').find_next('ul', class_='p_tail').li.nextSibling.text
# print post_time.strip()
# #
# post_content = soup.find('cc').find_next('div').text
# print post_content.strip()


# jsonStr = soup.find('div', class_=re.compile(r'l_post\s+\w+|\w*\s*'))['data-field']
# print jsonStr
#
# datafield = json.loads(jsonStr)
# print datafield.keys()
# print datafield['author']['user_name']
# print datafield['author']['name_u'].decode('gbk')
# print datafield['author']['level_name']
# print datafield['content']['open_type']
# print datafield['content']['date']
# print datafield['content']['post_no']
# print type(datafield)
#
# datas = []
# datas.append(datafield)
#
# for data in datas:
#     print data['author']['user_name']


# index = 40
# for i in range(int(index)):
#     print i

 #创建链接
client = MongoClient('127.0.0.1', 27017)

#选择tieba数据库
db = client.test # new a database
db.add_user('test', 'test') # add a user
db.authenticate('test', 'test') # check auth

muser = db.user # new a table
muser.save({'id':1, 'name':'test'}) #add a record
muser.insert({'id':2, 'name':'hello'}) #add a record
muser.find_one() #find a record
muser.find_one({'id':2}) # find a record by query


