# -*- coding: utf-8 -*-
#协议模板，照此格式填代码

ENCODING = 'gbk'

import kit
from urllib.request import urlopen

def introduce():
	return '''XXX.com(XXX)
链接类似这样：XXX'''

def getcontext(url):
	'''获取书籍目录，参数为目录页面，返回书籍名，作者，书籍id，书籍介绍与一个由二项元组组成的列表，元组第一项为链接，第二项为章节标题'''
	kit.logger(0, '打开小说目录页(%s)' % url)
	
	kit.logger(0, '整理章节内容来源')
	
	kit.logger(0, '整理完毕，共有%d章' % len(step2))

def getchapter(url):
	'''获取章节内容，参数为该章节页面，返回章节内容（html）'''
	pass

def search(keyword):
	'''搜索书籍，参数为关键字，返回一个由二项元组组成的列表，元组第一项为链接，第二项为书籍名称'''
	pass
