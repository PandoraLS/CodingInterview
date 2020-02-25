# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/2/23 12:06
from functools import reduce
import operator


class Solution:
    def maxProduct(self, nums):

        tmp_product = nums[0]

        def dfs(rest, begin):
            if not rest:
                return tmp_product
            sub_nums = []
            for i in range(begin + 1, len(rest) + 1):
                multi = reduce(operator.mul, nums[begin, i])
                
                if multi > tmp_product:
                    sub_nums.append(nums[begin, i])

        pass


if __name__ == '__main__':
    so = Solution()
    nums = [2, 3, -2, 4]
    print(so.maxProduct(nums))
