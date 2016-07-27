#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#测试用例
import kit

datestr = datetime.now().strftime('%Y%m%d%H%M%S')

kit.logger(0, datestr, '这是日志')
kit.logger(1, datestr, '这是警告')
kit.logger(-1, datestr, '这是错误')
