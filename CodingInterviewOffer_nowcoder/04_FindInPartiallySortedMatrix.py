# -*- coding: utf-8 -*-
# @Time    : 2019/9/17 16:53
# @Author  : Li Sen

"""
面试题4：二维数组中的查找
题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""

class Solution:
    def Find(self, target, array):
        '简单粗暴，二层遍历，时间不是最优'
        found = False
        rows, columns = len(array),len(array[0])
        if array and rows > 0 and columns > 0:
            for row in range(rows):
                for column in range(columns):
                    if array[row][column] == target:
                        found = True
        return found
    
    def Find2(self, target, array):
        '从右上角开始判断'
        found = False
        rows = len(array)
        columns = len(array[0])
        if array and rows > 0 and columns > 0:
            row = 0
            column = columns - 1
            while row < rows and column >= 0:
                if array[row][column] == target:
                    found = True
                    break
                elif array[row][column] > target:
                    column -= 1
                else:
                    row += 1
        return found
    
    def Find3(self, target, array):
        '从左下角开始判断'
        found = False
        rows = len(array)
        columns = len(array[0])
        if array and rows > 0 and columns > 0:
            row = rows -1
            column = 0
            while row >= 0 and column < columns:
                if array[row][column] == target:
                    found = True
                    break
                elif array[row][column] > target:
                    row -= 1
                else:
                    column += 1
        return found

if __name__ == "__main__":
    Array = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13],
             [6, 8, 11, 15]]
    Target = 7
    print(Solution().Find(Target, Array))
    print(Solution().Find2(Target, Array))
    print(Solution().Find3(Target, Array))
    