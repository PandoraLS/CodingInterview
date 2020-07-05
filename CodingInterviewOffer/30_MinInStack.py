# -*- coding: utf-8 -*-
# @Time    : 2019/12/5 21:41
# @Author  : Li Sen


"""
// 面试题30：包含min函数的栈
// 题目：定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的min
// 函数。在该栈中，调用min、push及pop的时间复杂度都是O(1)。
链接：https://www.nowcoder.com/questionTerminal/4c776177d2c04c2494f2555c9fcc1e49
来源：牛客网
思路：利用一个辅助栈来存放最小值

    栈  3，4，2，5，1
    辅助栈 3，3，2，2，1
每入栈一次，就与辅助栈顶比较大小，如果小就入栈，如果大就入栈当前的辅助栈顶
当出栈时，辅助栈也要出栈
这种做法可以保证辅助栈顶一定都当前栈的最小值
"""


class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, node):
        self.stack.append(node)
        if not self.min_stack or node <= self.min_stack[-1]:
            self.min_stack.append(node)

    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.min_stack[-1]
