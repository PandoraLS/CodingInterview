# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/2/29 18:00

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        from bisect import bisect_left
        for row in matrix:
            i = bisect_left(row,target) # 二分查找
            if i != len(row) and row[i] == target:
                return True
        return False