# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/1/13 11:18

class Solution:
    def StrToInt(self, s):
        # write code here
        numlist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-']
        sum = 0
        label = 1  # 正负数标记
        if s == '':
            return 0
        if s == "-2147483649" or s == "2147483648": # 最小的负数与最大的正数
            return 0
        for string in s:
            if string in numlist:  # 如果是合法字符
                if string == '+':
                    label = 1
                    continue
                if string == '-':
                    label = -1
                    continue
                else:
                    sum = sum * 10 + numlist.index(string)
            if string not in numlist:  # 非合法字符
                sum = 0
                break  # 跳出循环
        return sum * label


if __name__ == '__main__':
    so = Solution()
    string = "-2147483649"
    print(so.StrToInt(string))
