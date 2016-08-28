#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  novel_pachong.py
#  本工具为Hyello的御用网络爬虫，专用于网络小说爬取。
#  小说版权归原作者所有 本程序基于Python3
#  Copyright 2016 Hyello Songer <hyello@hyello-tpc>
#  
#  本程序为自由软件; 你可以在自由软件基金会发布的GNU通用公共许可证
#  （第2版或任何更新的版本）条款约束下重发布或（和）修改本程序。
from urllib.request import urlopen
#from html.parser import HTMLParser
from define import snwx, biquge, leduwo, snwx_txt, kanunu
df = {'snwx':snwx, 'leduwo':leduwo, 'biquge':biquge, 'snwx_txt':snwx_txt, 'kanunu':kanunu}
from datetime import datetime
import os
import kit

print('''------------------------
Pachong Ver003
Author:Hyello Songer
Website:hyello.org
-----------------------
''')

print('------------------')
for j in df.values():
	print(' - ' + j.introduce())
print('------------------')

src = str(input('请输入书籍源（括号内标识符）：'))
ctx_add = str(input('请输入书籍目录地址：'))
flag_h1 = bool(input('是否将目录中的大标题写入文件（1为是，0为否，或其他有效的逻辑值）：'))
kit.logger(kit.LOG, '书籍源%s %s' % (src, ctx_add))
try:
	book_name, author, book_id, introduce, context = df[src].getcontext(ctx_add)
except:
	kit.logger(kit.ERR, '%s不是合法的书籍源' % src)


kit.logger(kit.LOG, '向"%s"文件夹输出开始' % book_name)
ctn = [] #ctn = [(local_name, chapter_title, online_link)]
flag_continue = False
try:
	os.mkdir('./' + book_name)
except FileExistsError:
	kit.logger(kit.WARN, '\"%s\"文件夹已存在' % book_name)
	try:
		if 'content.txt' in os.listdir('./' + book_name):
			kit.logger(kit.LOG, '尝试读取content.txt')
			with open('./%s/content.txt' % book_name, 'r') as file_ctn:
				ctn = [tuple(x.replace('\n', '').split('|')) for x in file_ctn.readlines() if x != '\n']
				#print(repr(ctn))
				kit.logger(kit.LOG, '上次最后下载到：%s' % ctn[-1][1])
				flag_continue = bool(input('请决定是否从上次位置开始（已经下载的章节将不会再次下载）？\n（1为是，0为否，或其他有效的逻辑值）：'))
	except:
		pass

if not ('introduction.html' in os.listdir('./' + book_name) and flag_continue):
	with open('./%s/introduction.html' % book_name, 'w') as file_intro:
		file_intro.write('<html><head><meta charset=\"utf-8\" /><title>%s</title></head><body>\n' % book_name)
		file_intro.write("<p align=\'right\'><em>书名：" + book_name + ' 作者：' + author + \
		'<br />本文件系Songer小说爬虫自动生成<br />' + introduce + '\n</em></p>' + \
		'</body></html>')

i = 0
bitee = len(str(len(context)))
file_ctn = open('./%s/content.txt' % book_name, 'a')
for link, title in context:
	i += 1
	if not(link in [j[2] for j in ctn] and flag_continue):
		kit.logger(kit.LOG, 'Skip:%s %s' % (link, title))
		continue
	filename = ('chapter%.' + str(bitee) + 'd.html') % i
	with open(('./%s/' + filename) % book_name, 'w') as file_chap:
		try:
			file_chap.write('<html><head><style>p{text-indent:2em;margin:1px auto 1px auto;}</style>\n<meta charset=\"utf-8\" /><title>%s - %s</title></head><body>\n' % (book_name, title))
			if link == kit.H1_SIGN and flag_h1:
				file_chap.write('<br />' * 3 + '<h1 align=\center\">' + title + '</h1>\n' + '<br />' * 3)
				kit.logger(kit.LOG, '（大标题）%s' % title)
			else:
				file_chap.write('<h2>' + title + '</h2><hr />\n' + df[src].getchapter(link))
				kit.logger(kit.LOG, '%s %s' % (link, title))
			file_chap.write('</body></html>')
			file_ctn.write('%s|%s|%s\n' % (filename, title, link))
		except:
			file_chap.write('<h2>' + title + \
			'</h2><hr />\n本章节的内容好像出了点问题，请手动处理！'\
			+ '<a href=\"' + link + '\">章节链接</a>')
			kit.logger(kit.WARN, '章节获取失败:%s %s' % (link, title))

kit.logger(kit.LOG, '向"%s"文件夹输出结束' % book_name)
