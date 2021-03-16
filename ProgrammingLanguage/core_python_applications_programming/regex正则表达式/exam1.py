# -*- coding: utf-8 -*-
import re

content = 'Hello 1234567 is a number. Regex String'
result = re.match('^Hello ([0-9]+).*String$', content)
# "^Hello " 匹配字符串开头; (\d+) 匹配任意个数字; .* 匹配任意字符(换行符除外); 
# String$ 匹配字符串结尾
if result:
    print(result.group())
    print(result.groups())
    print(result.group(1)) # 取出第一个括号的内容, 即(\d+)中的数字
    
# 取出字符串中的数字
# re.match(pattern, string, flags=0)
# # pattern     匹配的正则表达式
# # string      要匹配的字符串
# # flags	      标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等