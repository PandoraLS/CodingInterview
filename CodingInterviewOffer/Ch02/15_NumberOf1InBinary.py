# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 21:08
# @Author  : Li Sen

"""
// 面试题15：二进制中1的个数
// 题目：请实现一个函数，输入一个整数，输出该数二进制表示中1的个数。例如
// 把9表示成二进制是1001，有2位是1。因此如果输入9，该函数输出2。
"""


class Solution:
    def NumberOf1(self, n):
        # 最佳解法
        count = 0
        if n < 0: # 如果该整数是负数，要把它和0xffffffff相与，消除负数的影响。
            n = n & 0xffffffff
        while n:
            n = (n - 1) & n
            count += 1
        return count

    def NumberOf1_2(self, n):
        # 解法2 使用python特性
        return bin(n & 0xffffffff).count("1")


if __name__ == '__main__':
    so = Solution()
    print(so.NumberOf1(9))
    print(so.NumberOf1_2(9))
