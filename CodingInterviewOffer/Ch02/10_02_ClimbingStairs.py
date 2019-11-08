# -*- coding: utf-8 -*-
# @Time    : 2019/11/8 17:42
# @Author  : Li Sen

# 青蛙跳台阶问题，一只青蛙要跳上n层高的台阶，一次能跳一级，也可以跳两级，请问这只青蛙有多少种跳上这个n层高台阶的方法？
# 1、2、3、5、8、13、21、34

class Solution:
    def Fibonacci(self, n):
        # write code here
        result = [1, 2]
        if n < 2:
            return result[n]
        fibNMinusOne = 1
        fibNMinusTwo = 2
        fibN = 0
        for i in range(2, n):
            fibN = fibNMinusOne + fibNMinusTwo
            fibNMinusOne = fibNMinusTwo
            fibNMinusTwo = fibN
        return fibN


if __name__ == '__main__':
    n = 8
    F = Solution()
    print(F.Fibonacci(n))
