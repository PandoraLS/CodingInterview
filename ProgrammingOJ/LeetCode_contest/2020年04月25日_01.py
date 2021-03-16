# -*- coding: utf-8 -*-
# @Time : 2020/4/25 15:05
from typing import List
class Solution:
    def expectNumber(self, scores: List[int]) -> int:
        pass
    def permutation(self, nums):
        res = []

        def dfs(pos):
            if pos == len(nums) - 1:
                res.append(nums[:])
            fixed = set()
            for i in range(pos, len(nums)):
                if nums[i] in fixed:  # 每种字符在pos只会被固定一次，对重复方案进行剪枝
                    continue
                fixed.add(nums[i])
                nums[i], nums[pos] = nums[pos], nums[i]
                dfs(pos + 1)
                nums[i], nums[pos] = nums[pos], nums[i]  # 回溯

        dfs(0)
        return res


if __name__ == '__main__':
    nums = [1,1,2]
    nums.sort(reverse=True)
    so = Solution()
    print(so.permutation(nums))