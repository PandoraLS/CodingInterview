# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/2/25 21:20
class Solution:
    # 动态规划
    def maxProfit(self, prices, fee: int) -> int:
        n = len(prices)
        if not prices:
            return 0
        hold = [0 for i in range(n)]
        not_hold = [0 for i in range(n)]
        hold[0] = -prices[0]  # 第0天持有
        not_hold[0] = 0  # 第0天不持有
        for i in range(1, n):
            hold[i] = max(hold[i - 1], not_hold[i - 1] - prices[i])
            # 今天持有，要么就是昨天持有今天继续保持；要么就是昨天没有今天买入
            not_hold[i] = max(not_hold[i - 1], hold[i - 1] + prices[i] - fee)
            # 今天没有，要么是昨天就没有有今天继续保持；要么是昨天持有，今天卖出，顺便把手续费交了
        return not_hold[n - 1]
class Solution2:
    # labuladong的算法小抄
    def maxProfit(self, prices, fee: int) -> int:
        dp_i_0, dp_i_1 = 0, float('-inf')
        for i in range(len(prices)):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, temp - prices[i] - fee)
        return dp_i_0


if __name__ == '__main__':
    so = Solution()
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    print(so.maxProfit(prices, fee))
