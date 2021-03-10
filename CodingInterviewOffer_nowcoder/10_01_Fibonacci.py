# -*- coding: utf-8 -*-
# @Time    : 2019/11/8 17:03
# @Author  : Li Sen

# 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。 # n<=39
# 1、1、2、3、5、8、13、21、34

class Solution:
    def Fibonacci(self, n):
        # write code here
        result = [0, 1]
        if n < 2:
            return result[n]
        fibNMinusOne = 0
        fibNMinusTwo = 1
        fibN = 0
        for i in range(2, n + 1):
            fibN = fibNMinusOne + fibNMinusTwo
            fibNMinusOne = fibNMinusTwo
            fibNMinusTwo = fibN
        return fibN


if __name__ == '__main__':
    n = 8
    F = Solution()
    print(F.Fibonacci(n))
