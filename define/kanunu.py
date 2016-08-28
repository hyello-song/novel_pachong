# -*- coding: utf-8 -*-
#kanunu协议

ENCODING = 'gbk'

import kit
from urllib.request import urlopen

def introduce():
	return '''kanunu8.com(kanunu)
链接类似这样：http://www.kanunu8.com/files/world/201102/1598.html
http://www.kanunu8.com/book3/8365/index.html'''

def getcontext(url):
	'''获取书籍目录，参数为目录页面，返回书籍名，作者，书籍id，书籍介绍与一个由二项元组组成的列表，元组第一项为链接，第二项为章节标题'''
	kit.logger(0, '打开小说目录页(%s)' % url)
	with urlopen(url) as file_obj:
		list_raw = file_obj.read()
		list_str = list_raw.decode(ENCODING, 'replace')
		if 'files' in url:
			srctype = 0
			step1 = kit.pickout(list_str, '<table cellspacing=', '</table>')
		elif '/book' in url:
			srctype = 1
			step1 = kit.pickout(list_str, '<table cellspacing=', '</table>')
		else:
			srctype = 1
			step1 = kit.pickout(list_str, '<table border="0" cellspacing=\"1\" cellpadding=\"7\"', '</table>')
	step2 = []
	kit.logger(0, '整理章节内容来源')
	for i in step1.split('</td>'):
		try:
			if '<tr align=\"center\" bgcolor=\"#ffffcc\">' in i:
				step2.append((kit.H1_SIGN, kit.pickout(i, '<strong>', '</strong>')))
			else:
				step2.append((url[0:url.rindex('/') + 1] \
				+ kit.pickout(i, '<a href=\"', '\">'), \
				kit.pickout(i, 'html\">', '</a>')))
		except:
			kit.logger(1, '割目录结构出错(%s)' % i)
	kit.logger(0, '整理完毕，共有%d章' % len(step2))
	if '<td class=\"p10-21\">' in list_str:
		context = kit.pickout(list_str, '<td class=\"p10-21\">', '</td>')
	elif '<td class=\"p10-24\">' in list_str:
		context = kit.pickout(list_str, '<td class=\"p10-24\">', '</td>')
	else:
		context = ""
	if srctype == 0:
		bk_name = kit.pickout(list_str, '<h2><b>', '</b></h2>')
		bk_id = kit.pickout(url, 'files/', '.html')
	elif srctype == 1:
		bk_name = kit.pickout(list_str, '<font color=\"#dc143c\">', '</font>')
		bk_id = kit.pickout(url, '/book', '/index.html')
	else:
		bk_name = ""
		bk_id = ""
	return bk_name, kit.pickout(list_str, '作者：', ' 发布时间'), \
	bk_id, context, step2

def getchapter(url, flag = 0):
	'''获取章节内容，参数为该章节页面，返回章节内容（html）'''
	return '<p>' + kit.pickout(urlopen(url).read().decode(ENCODING, 'replace'), '<td width=\"820\" align=\"left\" bgcolor=\"#FFFFFF\">', '</td>').\
	replace('<br />\r\n<br />', '</p><p>').replace('&nbsp;&nbsp;', '').replace('　　', '') + '</p>\n'

def search():
	'''搜索书籍，参数为关键字，返回一个由二项元组组成的列表，元组第一项为链接，第二项为书籍名称'''
	pass
