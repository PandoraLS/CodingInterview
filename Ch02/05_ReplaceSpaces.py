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
        """
        剑指offer解法：
        ①先计算源字符串数组长度，并统计空格数量
        ②新字符串数组长度=源数组长度+2*空格数量
        ③在新字符串数组上，从后向前遍历，通过两个index移动并复制
        :param s: 输入字符串s
        :return: 替换后的字符串
        """
        if s == "" or len(s) <= 0:
            return ""

        # 计算空格数量
        s = list(s)
        count = 0
        for i in s:
            if i == " ":
                count += 1

        p1 = len(s) - 1  # p1初始化为原始字符串数组末尾的index

        s += [None] * (count * 2)  # 将s扩充为新长度
        p2 = len(s) - 1  # p2初始化为新字符串数组末尾的index
        while p1 >= 0:
            if s[p1] == ' ':
                for i in ['0', '2', '%']:
                    s[p2] = i
                    p2 -= 1
            else:
                s[p2] = s[p1]
                p2 -= 1
            p1 -= 1
        return ''.join(s)


if __name__ == "__main__":
    S = "We Are Happy"
    print(Solution().replaceSpace1(S))
    print(Solution().replaceSpace2(S))
    print(Solution().replaceSpace3(S))
