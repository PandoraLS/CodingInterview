# -*- coding: utf-8 -*-
import re

# findall() 会搜索字符串，以列表形式返回全部能匹配的子串。
# 
# findall(pattern, string, flags=0)

# 取出html中的歌手名和歌名
html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''

# 使用search
result = re.search('<a.*?singer="(.*?)">(.*?)</a>', html)
# 歌手名和歌名都在<a>标签中, 从 <a 开始匹配
if result:
    print(result)
    print(result.groups())
    print('--------------------------')
    print(result.group(1), result.group(2))
# 
# 输出结果
# 任贤齐 沧海一声笑   
# search只能返回匹配到的第一个结果

# 使用findall
result = re.findall('<a.*?singer="(.*?)">(.*?)</a>', html)
if result:
    print(result)