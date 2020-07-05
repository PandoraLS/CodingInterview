# -*- coding: utf-8 -*-
# Author：lisen
# Date：2020/1/5 20:41

class Solution:
    def getMaxValue(self, array, rows, cols):
        if array == [] or rows <= 0 or cols <= 0:
            return 0
        maxValues = [[0 for i in range(cols)] for j in range(rows)]
        for i in range(rows):
            for j in range(cols):
                left = 0
                up = 0
                if i > 0:  # 如果行号大于0，说明它上面有数字
                    up = maxValues[i - 1][j]
                if j > 0:  # 如果列号大于0，说明它左边有数字
                    left = maxValues[i][j - 1]
                maxValues[i][j] = max(up, left) + array[i * cols + j]

        return maxValues[rows - 1][cols - 1]


if __name__ == '__main__':
    so = Solution()
    array = [1, 10, 3, 8, 12, 2, 9, 6, 5, 7, 4, 11, 3, 7, 16, 5]
    print(so.getMaxValue(array, rows=4, cols=4))
