# -*- coding: utf-8 -*-
# match和search对比
import re

content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result = re.match('Hello.*?(\d+).*?Demo', content)
print(result)
# match没有匹配, 字符串不是Extra开头
print('------------------------')
result = re.search('Hello.*?(\d+).*?Demo', content)
print(result.group(1))