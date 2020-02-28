# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/2/23 12:06
from functools import reduce
import operator


# 题解：https://leetcode-cn.com/problems/maximum-product-subarray/solution/hua-jie-suan-fa-152-cheng-ji-zui-da-zi-xu-lie-by-g/
class Solution:
    def maxProduct(self, nums):
        max_res, imax, imin = float('-inf'), 1, 1
        for i in range(len(nums)):
            if nums[i] < 0:
                imax, imin = imin, imax
            imax = max(imax * nums[i], nums[i])
            imin = min(imin * nums[i], nums[i])
            max_res = max(max_res, imax)
        return max_res


if __name__ == '__main__':
    so = Solution()
    nums = [2, 3, -2, 4]
    print(so.maxProduct(nums))
    nums2 = [2, 3, -2, 4, -2]
    print(so.maxProduct(nums2))
