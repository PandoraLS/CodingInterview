# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/1/10 16:13


"""
题目：https://www.acwing.com/problem/content/76/
解答：https://github.com/darkTianTian/sword-for-offer/tree/master/chapter_6/section_4#60-n%E4%B8%AA%E9%AA%B0%E5%AD%90%E7%9A%84%E7%82%B9%E6%95%B0

将一个骰子投掷n次，获得的总点数为s，s的可能范围为n~6n。
掷出某一点数，可能有多种掷法，例如投掷2次，掷出3点，共有[1,2],[2,1]两种掷法。
请求出投掷n次，掷出n~6n点分别有多少种掷法。
样例1
输入：n=1
输出：[1, 1, 1, 1, 1, 1]
解释：投掷1次，可能出现的点数为1-6，共计6种。每种点数都只有1种掷法。所以输出[1, 1, 1, 1, 1, 1]。
样例2
输入：n=2
输出：[1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
解释：投掷2次，可能出现的点数为2-12，共计11种。每种点数可能掷法数目分别为1,2,3,4,5,6,5,4,3,2,1。
所以输出[1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]。
"""


class Solution(object):
    def numberOfDice(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        f = [[0 for _ in range(6 * n + 1)] for _ in range(n + 1)]
        for i in range(1, 7):  # 初始状态为1
            f[1][i] = 1
        for i in range(2, n + 1):
            for j in range(i, 6 * i + 1): # j代表了求和的结果
                for k in range(1, min(j, 6) + 1):
                    f[i][j] += f[i - 1][j - k]  # 上一次抛掷target为j - k时的状态

        for i in range(n, n * 6 + 1):
            res.append(f[n][i])  # 第n次抛掷时值为i的次数
        return res


if __name__ == '__main__':
    so = Solution()
    print(so.numberOfDice(3))
