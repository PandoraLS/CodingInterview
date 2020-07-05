# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/1/10 19:11

class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if not m or not n:
            return -1
        res = list(range(n))
        i = 0
        while len(res) > 1:
            i = (m + i - 1) % len(res)
            res.pop(i)
        return res[0]


if __name__ == '__main__':
    so = Solution()
    print(so.LastRemaining_Solution(5, 3))
