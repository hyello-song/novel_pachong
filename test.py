#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 我是测试用例

import kit
from define import snwx, snwx_txt, leduwo, kanunu
from datetime import datetime

kit.datestr = datetime.now().strftime('%Y%m%d%H%M%S')
#日志功能
kit.logger(0, '这是日志')
try:
	i = 0 / 0
except:
	kit.logger(1, '这是除零错警告')

#字符串截取功能
TESTSTR = '''<a href="10379.html">ddf</a>
<script>var pick = 0;
var diff = 'hahaha';
</script>
'''

assert kit.pickout(TESTSTR, '<a href=\"', '\"') == '10379.html'
assert kit.pickout(TESTSTR, "var diff = \'", "\';") == 'hahaha'

#真刀真枪
def test_define(df, url, bn, au, bid):
	book_name, author, book_id, introduce, context = df.getcontext(url)
	print(book_name, author, book_id)
	assert book_name == bn and author == au and book_id == bid
	print('Indroduction:', introduce)
	print(context[2][1], '\n', df.getchapter(context[2][0]))

test_define(snwx, 'http://www.snwx.com/book/6/6651/', '斗罗大陆', '唐家三少', '6651')
test_define(snwx_txt, 'http://www.snwx.com/txt/6651.html', '斗罗大陆', '', '6651')
test_define(leduwo, 'http://www.leduwo.com/book/1/1534/', '冰火魔厨', '唐家三少', '1534')
test_define(kanunu, 'http://www.kanunu8.com/files/world/201102/1598.html', '苏菲的世界', '乔斯坦・贾德', 'world/201102/1598')


try:
	j = int('This is not a number')
except:
	kit.logger(-1, '这是错误')


