# -*- coding: utf-8 -*-
# 改进1.2的匹配模式（非贪婪模式）
import re

content = 'Hello 1234567 is a number. Regex String'
result = re.match('.*?(\d+).*', content)
# 在 .* 后面加 ? 就可以使用非贪婪模式
if result:
    print(result)
    print(result.groups())
    print(result.group())
    print(result.group(1))
    print(result.groups())
