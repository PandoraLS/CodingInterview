# -*- coding: utf-8 -*-
# Author：lisen
# Date：2020/1/4 16:06

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        n = len(array)
        dp = [i for i in array]  # dp[i]表示以元素array[i]结尾的最大连续子数组和
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + array[i], array[i])
        return max(dp)


if __name__ == '__main__':
    array = [-2, -3, 4, -1, -2, 1, 5, -3]
    so = Solution()
    print(so.FindGreatestSumOfSubArray(array))
