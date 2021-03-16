# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/3/3 7:48

from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        stack = list()
        op = '+'
        for i, c in enumerate(s):
            if c.isnumeric():
                num = num * 10 + int(c) # 处理不是个位数的情况
            if c in '+-*/' or i == len(s) - 1:
                if op == '+': # 这里op存放的是上一个运算符
                    stack.append(num)
                if op == '-':
                    stack.append(-num)
                if op == '*':
                    stack.append(stack.pop() * num)
                if op == '/':
                    stack.append(int(stack.pop() / num))
                op = c
                num = 0
        return sum(stack)


if __name__ == '__main__':
    so = Solution()
    string = "1 + 2* 3-2"
    print(so.calculate(string))
