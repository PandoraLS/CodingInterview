# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/3/9 16:20
from typing import List


class LargetNumKey(str):
    def __lt__(x, y):
        return x + y < y + x


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if set(nums) == {0}: return '0'
        str_nums = sorted([str(i) for i in nums], key=LargetNumKey)
        res = ''
        while str_nums:
            res += str_nums[-1]
            del str_nums[-1]
        return res


from functools import cmp_to_key


class Solution2:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(x, y):
            if x == y:
                return 0
            elif x + y < y + x:
                return 1 # 返回1的时候，会颠倒x和y的顺序来排序
            else:
                return -1 # 返回-1的时候，保持原有顺序不变

        res = ''.join(sorted(map(str, nums), key=cmp_to_key(cmp)))
        return '0' if res[0] == '0' else res


if __name__ == '__main__':
    so = Solution()
    nums = [3, 30, 34, 5, 9]
    print(so.largestNumber(nums))
    so2 = Solution2()
    print(so2.largestNumber(nums))
