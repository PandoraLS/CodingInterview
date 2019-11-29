# -*- coding: utf-8 -*-
# @Time    : 2019/11/29 16:30
# @Author  : Li Sen
import re


class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        # 利用python的强制类型转换
        try:
            p = float(s)
            return True
        except:
            return False

    def isNumeric2(self, s):
        # 使用正则表达式

        # [\\+\\-]?               -> 正或负符号出现与否
        # \\d*                     -> 整数部分是否出现，如 -.34或 +3.34均符合
        # (\\.\\d*)?              -> 是否出现小数点，小数点后的数字可以没有
        # ([eE][\\+\\-]?\\d+)?    -> 如果存在指数部分，那么e或E肯定出现，+或 - 可以不出现，紧接着必须跟着整数；或者整个部分都不出现

        # 下面的正则表达式都是通过了的
        # x = "([+-])?(\d)*([.](\d)*)?([eE][+-]?(\d)+)?"
        # x = "[\\+\\-]?\\d*(\\.\\d+)?([eE][\\+\\-]?\\d+)?"
        # x = "[\\+\\-]?\\d*(\\.\\d*)?([eE][\\+\\-]?\\d+)?"
        x = "[\\+-]?\d*(\\.\d*)?([eE][\\+-]?\d+)?"
        pi = re.match(x, s)
        if pi.group() == s:
            return True
        else:
            return False


if __name__ == '__main__':
    s = "1a3.14"
    so = Solution()
    print(so.isNumeric(s))
    print(so.isNumeric2(s))
