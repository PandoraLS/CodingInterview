# -*- coding: utf-8 -*-
# @Time : 2020/4/26 10:51
"""
思路: 类似于剑指offer面试题66题. 构建乘积数组,使用左dp记录左起0的个数,右dp记录右起1的个数
最终结果是左起dp和右起dp的组合中最大的那个
"""

class Solution:
    def maxScore(self, s: str) -> int:
        if s == "":
            return 0
        n = len(s)
        dp_left, dp_right, res = [0] * n, [0] * n, [0] *n

        if s[0] == '0':
            dp_left[0] = 1
        for i in range(1, n):
            if s[i] == '0': dp_left[i] = dp_left[i-1] + 1
            else:           dp_left[i] = dp_left[i-1]
        print(dp_left)

        if s[-1] == '1':
            dp_right[-1] = 1
        for i in range(n-2, -1, -1): # 从后往前,不包括最右侧的数
            if s[i] == '1': dp_right[i] = dp_right[i + 1] + 1
            else:         dp_right[i] = dp_right[i + 1]
        print(dp_right)

        res = 0
        max_value = res
        for i in range(n-1):
            res = dp_left[i] + dp_right[i + 1]
            if res > max_value:
                max_value = res
        return max_value






if __name__ == '__main__':
    s = "011101"
    so = Solution()
    print(so.maxScore(s))



