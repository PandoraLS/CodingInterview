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


class Solution2:
    def maxProduct(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        dp_max = [nums[0]] * n
        dp_min = [nums[0]] * n
        imax = nums[0]
        for i in range(1, n):
            dp_max[i] = max(dp_max[i-1]*nums[i], dp_min[i-1]*nums[i], nums[i])
            dp_min[i] = min(dp_max[i-1]*nums[i], dp_min[i-1]*nums[i], nums[i])
            imax = max(dp_max[i], imax)
        return imax

if __name__ == '__main__':
    so = Solution()
    nums = [2, 3, -2, 4]
    print(so.maxProduct(nums))
    nums2 = [2, 3, -2, 4, -2]
    print(so.maxProduct(nums2))
    
    print('--------------------')
    so = Solution2()
    nums = [2, 3, -2, 4]
    print(so.maxProduct(nums))
    nums2 = [2, 3, -2, 4, -2]
    print(so.maxProduct(nums2))
