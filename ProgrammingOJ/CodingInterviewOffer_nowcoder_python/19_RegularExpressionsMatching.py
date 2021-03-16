# -*- coding: utf-8 -*-
# @Time    : 2019/11/29 11:17
# @Author  : Li Sen

'''
题目：请实现一个函数用来匹配包括'.'和'*'的正则表达式。
模式中的字符'.'表示任意一个字符（不包括空字符！），而'*'表示它前面的字符可以出现任意次（包含0次）。 
在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
'''


class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if len(s) == 0 and len(pattern) == 0:  # 如果s与pattern都为空，则True
            return True
        elif len(s) != 0 and len(pattern) == 0:  # 如果s不为空，而pattern为空，则False
            return False
        elif len(s) == 0 and len(pattern) != 0:  # 如果s为空，而pattern不为空，则需要判断
            if len(pattern) > 1 and pattern[1] == "*":  # pattern中的第二个字符为*，则pattern后移两位继续比较
                return self.match(s, pattern[2:])
            else:
                return False
        else:  # s与pattern都不为空的情况
            if len(pattern) > 1 and pattern[1] == "*":  # pattern的第二个字符为*的情况
                if s[0] != pattern[0] and pattern[0] != ".":  # s与pattern的第一个元素不同，则s不变，pattern后移两位，相当于pattern前两位当成空
                    return self.match(s, pattern[2])
                else:
                    # 如果s[0]与pattern[0]相同，且pattern[1]为*，这个时候有三种情况
                    # pattern后移2个，s不变；相当于把pattern前两位当成空，匹配后面的
                    # pattern后移2个，s后移1个；相当于pattern前两位与s[0]匹配
                    # pattern不变，s后移1个；相当于pattern前两位，与s中的多位进行匹配，因为*可以匹配多位
                    return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern)
            # pattern第二个字符不为*的情况
            else:
                if s[0] == pattern[0] or pattern[0] == ".":
                    return self.match(s[1:], pattern[1:])
                else:
                    return False

if __name__ == '__main__':
    so = Solution()
    s = 'baaab'
    pattern = 'ba*ab'
    print(so.match(s, pattern))
