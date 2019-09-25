# -*- coding: utf-8 -*-
# 多行匹配
import re

content = '''Hello is a number. 
                Regex String 1234567'''  # 把数字换到第二行
result = re.match('.*?(\d+).*', content)
# 在 .* 后面加 ? 就可以使用非贪婪模式
if result:
    print(result.groups())
    print(result.group(1))

# 没有输出结果
print('-----------------------------------')
result = re.match('.*?(\d+).*', content, flags=re.S)
# flags设置是否区分大小写，多行匹配等：re.S设置'.'可以匹配换行符, re.I忽略大小写...
if result:
    print(result.group(1))