#!/usr/bin/env python

import os
import re
# f = open('whodata','r')
f = os.popen('tasklist /nh', 'r') # 去除每一列的标题名
# strip(rm) 当rm为空时，默认删除空白符（包括'\n', '\r',  '\t',  ' ')
# f = os.popen('tasklist', 'r')
for eachLine in f:
    # print(r'\s\s+|\t',eachLine)
    # print(re.split(r'\s\s+',eachLine.rstrip()))
    # print(re.split(r'\s\s+', eachLine.strip()))
    # print(re.split(r'\s\s+|\t', eachLine.strip()))
    print (re.findall(
        '([\w.]+(?: [\w.]+)*)\s\s+(\d+) \w+\s\s+\d+\s\s+([\d,]+ K)',
        eachLine.rstrip()))
f.close()
