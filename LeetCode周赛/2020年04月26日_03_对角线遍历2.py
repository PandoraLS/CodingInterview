# -*- coding: utf-8 -*-
# @Time : 2020/5/5 11:19

"""
思路:这一题如果直接使用暴力模拟会超时
1. 遍历所有行列元素,以row+col作为键添加到matrix[row][col]值到列表中
2. 对字典进行排序,防止中间特别长导致row+col特别大,破坏字典插入有序性（由于不是矩阵,不可以直接
拿行列和去查询,因为键是跳跃的,如果这样会退化为暴力,所以排序）
3. 合并键值,返回结果
"""
from collections import defaultdict
from typing import List
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for row in range(len(nums) - 1, -1, -1):  # 倒序遍历
            for col in range(len(nums[row]) - 1, -1, -1):
                print(nums[row][col], end=" ")
                d[row + col].append(nums[row][col])
        print(d)
        res = []
        for idx in sorted(d):  # 对key进行排序
            res.extend(d[idx])
        return res

    def findDiagonalOrder2(self, nums: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for row in range(len(nums)):  # 如果正序遍历的话实际上是题目中每条线反过来
            for col in range(len(nums[row])):
                print(nums[row][col], end=" ")
                d[row + col].append(nums[row][col])
        print(d)
        res = []
        for idx in sorted(d):  # 对key进行排序
            res.extend(d[idx])
        return res


if __name__ == "__main__":
    nums = [[1,2,3],[4,5,6],[7,8,9]]
    so = Solution()
    print(so.findDiagonalOrder(nums))
    print('-----------------------')
    print(so.findDiagonalOrder2(nums))





