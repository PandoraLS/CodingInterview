# -*- coding: utf-8 -*-
# @Time : 2020/4/24 18:34

a = [1, 3, 5, 7, 10]

for i in range(len(a)):
    if not a[i] & 1:
        break
else:
    print('无偶数')