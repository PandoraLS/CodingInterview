# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/4/6 21:31

from typing import List


# 原问题：求出最长递增子序列的长度
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        max_val = max(dp)
        print(max_val)


"""
https://www.geeksforgeeks.org/construction-of-longest-increasing-subsequence-using-dynamic-programming/
打印最长子序列，稍微改了下，如果存在多条最长子序列，则都输出
"""
class Solution2:
    def printLIS(self, nums: List[int]):
        for num in nums:
            print(num, end=' ')
        print()

    def constructPrintLIS(self, nums: List[int], n: int):
        # l[i]: 以nums[i]结尾的最长递增子串，l中的每个元素都是list
        l = [[] for i in range(n)]
        # 初始化l[0]=nums[0]
        l[0].append(nums[0])
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                # l[i] = {max(L[j])} + nums[i]
                # where j < i and nums[j] < nums[i]
                if nums[j] < nums[i] and (len(l[i]) < len(l[j]) + 1):
                    dp[i] = max(dp[i], dp[j] + 1)
                    l[i] = l[j].copy()
            
            # l[i] ends with nums[i]
            l[i].append(nums[i])
        max_length = max(dp)
        for x in l:
            if len(x) == max_length:
                self.printLIS(x)

if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    so = Solution()
    so.lengthOfLIS(nums)
    so2 = Solution2()
    so2.constructPrintLIS(nums, len(nums))
