# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/1/10 21:45

class Solution:

    def __init__(self):
        self.sum = 0

    def Sum_Solution(self, n):
        # write code here
        def qiusum(n):
            self.sum += n
            n -= 1
            return n > 0 and self.Sum_Solution(n)

        qiusum(n)
        return self.sum
