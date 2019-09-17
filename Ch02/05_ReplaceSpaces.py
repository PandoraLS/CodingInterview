# -*- coding: utf-8 -*-
# @Time    : 2019/9/17 19:40
# @Author  : Li Sen


"""
面试题5：替换空格
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy，
则经过替换之后的字符串为We%20Are%20Happy。
"""


class Solution:
    # s 源字符串
    def replaceSpace1(self, s):
        '使用join'
        if s == "" or len(s) <= 0:
            return ""
        return "%20".join(s.split(" "))

    def replaceSpace2(self, s):
        '使用replace方法'
        if s == "" or len(s) <= 0:
            return ""
        return s.replace(" ", "%20")

    def replaceSpace3(self, s):
        '使用剑指offer书上的方法'
        if s == "" or len(s) <= 0:
            return ""
        


if __name__ == "__main__":
    S = "We Are Happy"
    print(Solution().replaceSpace1(S))
    print(Solution().replaceSpace2(S))
    print(Solution().replaceSpace3(S))
