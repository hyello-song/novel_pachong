# -*- coding: utf-8 -*-
ENCODING = 'gbk'

import kit
from urllib.request import urlopen

def introduce():
	return '''biquge.la(biquge)
书籍格式类似于这样：http://www.biquge.la/book/13453/
提示：可能会中途出错终止，这时重新打开本工具来过即可，之前下好的章节都会秒过'''

def getcontext(url):
	'''获取书籍目录，参数为目录页面，返回书籍名，作者，书籍id，书籍介绍与一个由二项元组组成的列表，元组第一项为链接，第二项为章节标题'''
	kit.logger(0, '打开小说目录页(%s)' % url)
	with urlopen(url) as file_obj:
		list_raw = file_obj.read()
		list_str = list_raw.decode(ENCODING, 'replace')
		step1 = kit.pickout(list_str, '<dl>', '</dl>')
	step2 = []
	kit.logger(0, '整理章节内容来源')
	for i in step1.split(r'</dd>'):
		try:
			step2.append((url + kit.pickout(i, '<a href=\"', '\">'), \
			kit.pickout(i, '\">', '</a>'))) 
		except:
			kit.logger(1, '割目录结构出错(%s)' % i)
		#print(step2[len(step2) - 1][0], step2[len(step2) - 1][1])
	kit.logger(0, '整理完毕，共有%d章' % len(step2))
	return kit.pickout(list_str, '<h1>', '</h1>'), \
	kit.pickout(list_str, '<meta property=\"og:novel:author\" content=\"', '\"/>'), \
	kit.pickout(list_str, 'var bookid = \"', '\";'), \
	kit.pickout(list_str, '<div id="intro">', '</div>'), step2

def getchapter(url):
	'''获取章节内容，参数为该章节页面，返回章节内容（html）'''
	try:
		return '<p>' + kit.pickout(urlopen(url).read().decode(ENCODING, 'replace'), \
		'<div id=\"content\"><script>readx();</script>', '</div>').replace('<br /><br />', '</p><p>').replace('&nbsp;&nbsp;', '') + '</p>\n'
	except:
		return '<p>' + kit.pickout(urlopen(url).read().decode(ENCODING, 'replace'), \
		'<div id=\"content\"><script>readx();</script>', '</div>').replace('<br /><br />', '</p><p>').replace('&nbsp;&nbsp;', '') + '</p>\n'

def search(keyword):
	'''搜索书籍，参数为关键字，返回一个由二项元组组成的列表，元组第一项为链接，第二项为书籍名称'''
	pass
