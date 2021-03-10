# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/1/9 20:40

class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if size <= 0:
            return []
        res = []
        for i in range(0, len(num) - size + 1):
            res.append(max(num[i:i + size]))
        return res
    

