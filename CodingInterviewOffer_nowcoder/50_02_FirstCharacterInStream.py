# -*- coding: utf-8 -*-
# Author：lisen
# Date：2020/1/6 15:19

"""
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，
第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
如果当前字符流没有存在出现一次的字符，返回#字符。
"""


class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ''
        self.dict = {}

    def FirstAppearingOnce(self):
        # write code here
        for i in self.s:
            if self.dict[i] == 1:
                return i
        return '#'

    def Insert(self, char):
        # write code here
        self.s = self.s + char
        if char in self.dict:
            self.dict[char] = self.dict[char] + 1
        else:
            self.dict[char] = 1


if __name__ == '__main__':
    so = Solution()
    so.Insert('g')
    print(so.FirstAppearingOnce())
    so.Insert('o')
    print(so.FirstAppearingOnce())
    so.Insert('o')
    print(so.FirstAppearingOnce())
    so.Insert('g')
    print(so.FirstAppearingOnce())
    so.Insert('l')
    print(so.FirstAppearingOnce())
    so.Insert('e')
    print(so.FirstAppearingOnce())
