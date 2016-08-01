# -*- coding: utf-8 -*-
#leduwo网站使用gbk编码
ENCODING = 'gbk'

import kit
from urllib.request import urlopen

def introduce():
	return '''leduwo.com(leduwo)
书籍地址类似于这样：http://www.leduwo.com/book/1/1534/'''

def getcontext(url):
	'''获取书籍目录，参数为目录页面，返回书籍名，作者，书籍id，书籍介绍与一个由二项元组组成的列表，元组第一项为链接，第二项为章节标题'''
	kit.logger(0, '打开小说目录页(%s)' % url)
	with urlopen(url) as file_obj:
		list_raw = file_obj.read()
		list_str = list_raw.decode(ENCODING, 'replace')
	#kit.pickout(list_str, '<div id=\"box\"><h1>', '</h1></div>') 书名
	#kit.pickout(list_str, '<a href=\"http://www.leduwo.com/modules/article/search.php?searchtype=author&searchkey=', '\" target=\"_blank\">')  作者
	step1 = kit.pickout(list_str, '<table', '</table>')
	step2 = []
	kit.logger(0, '整理章节内容来源')
	for i in step1.split('<td class=\"ccss\">'):
		try:
			step2.append((url + kit.pickout(i, '<a href=\"', '\">'), \
			kit.pickout(i, '\">', '</a>')))
		except:
			kit.logger(1, '割目录结构出错(%s)' % i)
	kit.logger(0, '整理完毕')
	return kit.pickout(list_str, '<div id=\"box\"><h1>', '</h1></div>'), \
	kit.pickout(list_str, '<a href=\"http://www.leduwo.com/modules/article/search.php?searchtype=author&searchkey=', '\" target=\"_blank\">'), \
	kit.pickout(list_str, 'var article_id = \"', '\";'), '（此功能未编写）', step2
	

def getchapter(url):
	'''获取章节内容，参数为该章节页面，返回章节内容（html）'''
	return kit.pickout(urlopen(url).read().decode(ENCODING, 'replace'), '<div id=\"content\">', '</div>').replace('<br /><br />', '<br />') + '\n'

def search(keyword):
	'''搜索书籍，参数为关键字，返回一个由二项元组组成的列表，元组第一项为链接，第二项为书籍名称'''
	pass
