# -*- coding: utf-8 -*-
# 练习爬虫实战练习
import requests
import re

content = requests.get('https://movie.douban.com/chart').text
# 豆瓣电影排行榜
# pattern = re.compile('class="pl2".*?<.*?="(.*?)".*?>(.*?)<span.*?>(.*?)</span>.*?"rating_nums">(.*?)</span>.*?"pl">(.*?)</span>', re.S)
pattern = re.compile(
    'class="pl2".*?<.*?="(.*?)".*?>(.*?)<span.*?>(.*?)</span>.*?"rating_nums">(.*?)</span>.*?"pl">(.*?)</span>', re.S)
# pattern = re.compile('class="pl2".*?<.*?="(.*?)".*?>(.*?)<span.*?>(.*?)</span>.*?"rating_nums">(.*?)</span>.*?"pl">(.*?)</span>', re.S)
# compile可以在多次使用中提高效率，这里影响不大
# print(content)
results = re.findall(pattern, content)
# results = re.findall('class="pl2".*?<.*?="(.*?)".*?>(.*?)<span.*?>(.*?)</span>.*?"rating_nums">(.*?)</span>.*?"pl">(.*?)</span>',re.S)#re.S设置'.'可以匹配换行符
for result in results:
    url, name1, name2, nums, pl = result
    # print(result)
    # print(url,name1,name2,nums,pl)
    # print(url,end='')
    # print(name1,end='')
    # print(name2,end='')
    # print(nums,end='')
    # print(pl)
    print(url, name1.replace("/", "").strip(), name2.replace("/", "").strip(), nums, pl)
    # print(url, name1.replace("/","").strip(), nums, pl)
print('---------------------')
# pattern2 = re.compile('class="pl2".*?<.*?="(.*?)".*?>(.*?)<span.*?"rating_nums">(.*?)</span>.*?"pl">(.*?)</span>', re.S)
# results2 = re.findall(pattern2, content)
# for result2 in results2:
#     url, name1, nums, pl = result2
#     print(url, name1.replace("/", "").strip(), nums, pl)
