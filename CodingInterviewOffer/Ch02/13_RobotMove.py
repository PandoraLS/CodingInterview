# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 12:56
# @Author  : Li Sen

"""
// 面试题13：机器人的运动范围
// 题目：地上有一个m行n列的方格。一个机器人从坐标(0, 0)的格子开始移动，它
// 每一次可以向左、右、上、下移动一格，但不能进入行坐标和列坐标的数位之和
// 大于k的格子。例如，当k为18时，机器人能够进入方格(35, 37)，因为3+5+3+7=18。
// 但它不能进入方格(35, 38)，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
"""


# 牛客网题解：https://www.nowcoder.com/questionTerminal/6e5207314b5241fb83f2329e89fdecc8?answerType=1&f=discussion

# 思路：这道题跟前一道题一样，也是回溯法，分析题目，我们需要两个全局变量：标志数组和计数变量；
# 需要一个函数来计算行坐标和列坐标的数位之和；终止条件包括三种情况：越界、重复、行坐标和列坐标的数位之和超过k，
# 然后流程和上一道题相同。

# 根据需求分析需要的函数或变量
# - 标志数组markmatrix和计数变量count
# - 计算行列坐标数位之和的函数
# - 包含计数与处理终止条件的函数

class Solution:
    def movingCount(self, threshold, rows, cols):
        if threshold < 0 or rows <= 0 or cols <= 0:
            return 0
        markmatrix = [False] * (rows * cols)
        count = self.movingCountCore(threshold, rows, cols, 0, 0, markmatrix)
        return count

    def movingCountCore(self, threshold, rows, cols, row, col, markmatrix):
        value = 0
        if self.check(threshold, rows, cols, row, col, markmatrix):
            markmatrix[row * cols + col] = True
            value = 1 + self.movingCountCore(threshold, rows, cols, row + 1, col, markmatrix) + \
                    self.movingCountCore(threshold, rows, cols, row - 1, col, markmatrix) + \
                    self.movingCountCore(threshold, rows, cols, row, col + 1, markmatrix) + \
                    self.movingCountCore(threshold, rows, cols, row, col - 1, markmatrix)
        return value

    def check(self, threhold, rows, cols, row, col, markmatrix):
        if (row >= 0 and row < rows and col >= 0 and col < cols and self.getDigitSum(row) + self.getDigitSum(
                col) <= threhold and not markmatrix[row * cols + col]):
            return True
        return False

    def getDigitSum(self, number):
        sum = 0
        while (number > 0):
            sum += number % 10
            number //= 10
        return sum


if __name__ == '__main__':
    solution = Solution()
    print(solution.movingCount(5, 10, 10))
