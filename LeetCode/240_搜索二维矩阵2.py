# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/2/19 14:58

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 这题用列表推导式比较麻烦难懂
        res = [True for mat in matrix for i in mat if i == target] # 如果找到i==target就记录为True
        return True if len(res) > 0 else False # 如果有True说明找到了这个点，


if __name__ == '__main__':
    so = Solution()
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    print(so.searchMatrix(matrix,100))