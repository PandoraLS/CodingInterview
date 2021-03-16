# -*- coding: utf-8 -*-
# @Time : 2020/4/25 7:55
"""
题目：https://leetcode-cn.com/problems/permutations/
"""
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(depth):
            if depth == len(nums) - 1:
                res.append(nums[:])
                # res.append(nums)  # 这么写是错误的，因为
            for i in range(depth, len(nums)):
                nums[i], nums[depth] = nums[depth], nums[i]
                dfs(depth+1)
                nums[i], nums[depth] = nums[depth], nums[i] # 回溯
        dfs(0)
        return res


if __name__ == '__main__':
    so = Solution()
    nums = [1, 2, 3]
    print(so.permute(nums))