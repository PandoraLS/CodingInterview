# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/1/12 15:13

# 加法是异或，进位是与<<1
# 题解 https://blog.csdn.net/lrs1353281004/article/details/87192205

class Solution:
    def Add(self, a, b):
        while (b):
            a, b = (a ^ b) & 0xFFFFFFFF, ((a & b) << 1) & 0xFFFFFFFF
        return a if a <= 0x7FFFFFFF else ~(a ^ 0xFFFFFFFF)
