# -*- coding: utf-8 -*-

# 改进exam1
import re

content = 'Hello 1234567 is a number. Regex String'
result = re.match('.*(\d+).*', content)
# 使用.*匹配其他所有字符, (\d+)匹配我们想要的数字
if result:
    print(result)
    print(result.groups())
    print(result.group(1))

# 贪婪模式
# 结果并不如我们想要的那样，只输出了最后一个数字
# 7 。原因是正则贪婪模式导致的，贪婪模式会匹配尽可能多的字符。" .* "
# 可以匹配所的字符，自然也包括了我们要的数字，所以它很贪婪的只给我们留一个
# 7 ，正好满足(\d +) 的匹配，真的很贪啊。
