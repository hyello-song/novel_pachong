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
from define import snwx, biquge, leduwo
df = {'snwx':snwx, 'leduwo':leduwo, 'biquge':biquge}
from datetime import datetime
import kit

print('''------------------------
Pachong Ver001
Author:Hyello Songer
Website:hyello.org
-----------------------
''')
kit.datestr = datetime.now().strftime('%Y%m%d%H%M%S')
print('''------------------
 - www.snwx.com(snwx)
 - leduwo.com(leduwo)
 - biquge.la(biquge)
------------------''')
src = str(input('请输入书籍源（括号内标识符）：'))
ctx_add = str(input('请输入书籍目录地址：'))
kit.logger(0, '书籍源%s %s' % (src, ctx_add))
try:
	book_name, context = df[src].getcontext(ctx_add)
except:
	kit.logger(-1, '%s不是合法的书籍源' % src)

with open('./' + book_name + '.html', 'w') as output:
	kit.logger(0, '向%s.html输出开始' % book_name)
	output.write('<html><head><meta charset=\"utf-8\" /><title>%s</title></head><body>' \
	% book_name)
	for j in context:
		try:
			output.write('<h1>' + j[1] + '</h1>\n' + df[src].getchapter(j[0]))
			kit.logger(0, '%s %s' % j)
		except:
			output.write('<h1>' + j[1] + \
			'</h1>\n本章节的内容好像出了点问题，请手动处理！'\
			+ '<a href=\"' + j[0] + '\">章节链接</a>')
			kit.logger(1, '章节获取失败:%s %s' % j)
	output.write('</body></html>')
	kit.logger(0, '向%s.html输出结束' % book_name)
