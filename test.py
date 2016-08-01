#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#测试用例
import kit
from datetime import datetime

kit.datestr = datetime.now().strftime('%Y%m%d%H%M%S')
#日志功能
kit.logger(0, '这是日志')
kit.logger(1, '这是警告')

#字符串截取功能
TESTSTR = '''<a href="10379.html">ddf</a>
<script>var pick = 0;
var diff = 'hahaha';
</script>
'''

assert kit.pickout(TESTSTR, '<a href=\"', '\"') == '10379.html'
assert kit.pickout(TESTSTR, "var diff = \'", "\';") == 'hahaha'

try:
	i = 0 / 0
except:
	kit.logger(-1, '这是错误')


