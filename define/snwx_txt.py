# -*- coding: utf-8 -*-
#snwx使用gbk编码
ENCODING = 'gbk'

import kit
from urllib.request import urlopen

def introduce():
	return '''www.snwx.com（txt下载页）(snwx_txt)
书籍地址类似于这样：http://www.snwx.com/txt/XXXX.html'''

def getcontext(url):
	'''获取书籍目录，参数为目录页面，返回书籍名，作者，书籍id，书籍介绍与一个由二项元组组成的列表，元组第一项为链接，第二项为章节标题'''
	kit.logger(0, '打开小说目录页(%s)' % url)
	with urlopen(url) as file_obj:
		list_raw = file_obj.read()
		list_str = list_raw.decode('gbk', 'replace')
		step1 = kit.pickout(list_str, '<ul>', '</ul>')
	step2 = []
	kit.logger(0, '整理章节内容来源')
	for i in step1.split(r'</li>'):
		try:
			step2.append((kit.pickout(i, 'href=\"', '\">'), kit.pickout(i, '">', '</a>'))) 
		except ValueError:
			kit.logger(1, '割目录结构出错(%s)' % i)
		#print(step2[len(step2) - 1][0], step2[len(step2) - 1][1])
	kit.logger(0, '整理完毕')
	return kit.pickout(list_str, '<DIV id="BookMl">', '<BR>'), \
	'', '', '（此功能未编写）', step2

def getchapter(url):
	'''获取章节内容，参数为该章节页面，返回章节内容（html）'''
	return kit.pickout(urlopen(url).read().decode('gbk', 'replace'), '<div id=\"BookText\">', '</div>').replace('<br /><br />', '<br />') + '\n'

def search(keyword):
	'''搜索书籍，参数为关键字，返回一个由二项元组组成的列表，元组第一项为链接，第二项为书籍名称'''
	pass
