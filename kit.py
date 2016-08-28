# -*- coding: utf-8 -*-
from datetime import datetime
import sys
datestr = datetime.now().strftime('%Y%m%d%H%M%S')
H1_SIGN = '@@@@'
KIT_ERR = -1
KIT_LOG = 0
KIT_WARN = 1

def pickout(target, start, end):
	poss = target.index(start)
	return target[poss + len(start):target.index(end, poss + len(start))]

#Songer的简单日志记录函数
#-1错误，0日志，1警告
#注意：必须先定义kit.datestr的值！
def logger(tp, text):
	with open("./" + datestr + ".txt", 'a') as log: #写入日志
		log.write(('@@@', '', '~~~')[tp + 1] + datetime.now().strftime('%Y年%m月%d日%H:%M:%S') + ' '
		+ ('ERR', 'LOG', 'WARN')[tp + 1] + ":" + text + "\n")
		if tp == -1 or tp == 1: #警告与错误一般会在异常引发的时候记录
			log.write('Additional Traceback:\n\t' \
			+ str(sys.exc_info()[0]) + str(sys.exc_info()[1]) + '\n')
	#控制台输出
	print(('@@@', '', '~~~')[tp + 1] + datetime.now().strftime('%Y年%m月%d日%H:%M:%S') + ' '
	+ ('ERR', 'LOG', 'WARN')[tp + 1] + ":" + text)
	if tp == -1 or tp == 1:
		print('Additional Traceback:\n\t', sys.exc_info()[0], sys.exc_info()[1])
	if tp == -1:
		exit(-1)


