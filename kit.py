# -*- coding: utf-8 -*-
from datetime import datetime

def pickout(target, start, end):
	poss = target.index(start)
	return target[poss + len(start):target.index(end, poss)]

#-1错误，0日志，1警告
def logger(tp, text):
	with open("./" + datestr + ".txt", 'a') as log:
		log.write(datetime.now().strftime('%Y年%m月%d日%H:%M:%S') + ' '
		+ ('@@@@@@@ERR', 'LOG', '~~~~~~~WARN')[tp + 1]
		+ ":" + text + ("@@@@@@@", "", "~~~~~~~")[tp + 1] + "\n")
	print(datetime.now().strftime('%Y年%m月%d日%H:%M:%S') + ' '
	+ ('@@@@@@@ERR', 'LOG', '~~~~~~~WARN')[tp + 1]
	+ ":" + text + ("@@@@@@@", "", "~~~~~~~")[tp + 1])
	if tp == -1:
		exit(-1)


