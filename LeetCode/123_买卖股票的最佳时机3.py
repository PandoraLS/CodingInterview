# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/2/24 12:09
class Solution:
    def maxProfit(self, prices) -> int:
        return self.max_profit_k(prices, 2)

    def max_profit_inf(self, prices):  # 
        n = len(prices)
        hold = -prices[0]
        not_hold = 0
        for i in range(1, n):
            prev_hold = hold
            hold = max(hold, not_hold - prices[i])
            not_hold = max(not_hold, prev_hold + prices[i])
        return not_hold

    def max_profit_k(self, prices, k):
        n = len(prices)
        if n == 0 or k == 0:
            return 0
        if k >= n / 2:
            return self.max_profit_inf(prices)

        hold = [[0 for i in range(k + 1)] for j in range(n)]
        not_hold = [[0 for i in range(k + 1)] for j in range(n)]

        for i in range(n):  # 天数
            for j in range(1, k + 1):  # 交易次数
                if i == 0:
                    hold[i][j] = -prices[i]
                    not_hold[i][j] = 0
                else:
                    not_hold[i][j] = max(not_hold[i - 1][j], hold[i - 1][j] + prices[i])
                    if j == 1:
                        hold[i][j] = max(hold[i - 1][j], -prices[i])  # 首次购买，选便宜的
                    else:
                        hold[i][j] = max(hold[i - 1][j], not_hold[i - 1][j - 1] - prices[i])
        return not_hold[n - 1][k]


if __name__ == '__main__':
    so = Solution()
    prices = [3, 2, 6, 5, 0, 3]
    print(so.maxProfit(prices))
