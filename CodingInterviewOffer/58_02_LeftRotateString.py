# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/1/9 19:57

class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        return s[n:] + s[:n]

    def reverse(self, s):
        if not s:
            return ""
        length = len(s)
        if length <= 0:
            return ""

        s = list(s)
        start = 0
        end = length - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return ''.join(s)

    def LeftRotateString2(self, s, n):
        if not s:
            return ""
        length = len(s)
        if length <= 0:
            return ""
        if n > length:
            n = n % length

        s = self.reverse(s)
        first = ''
        second = ''

        for i in range(length - n):
            first += s[i]
        first = self.reverse(first)
        for i in range(length - n, length):
            second += s[i]
        second = self.reverse(second)
        return first + second


if __name__ == '__main__':
    string = 'abcdefg'
    so = Solution()
    print(so.LeftRotateString(string, 2))
    print(so.LeftRotateString2(string, 2))
