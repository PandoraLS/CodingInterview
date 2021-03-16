# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/2/25 18:05

class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices) # 天数
        if not prices:
            return 0
        hold = [0 for i in range(n)]
        not_hold = [0 for i in range(n)]
        hold[0] = -prices[0]  # 第0天持有
        not_hold[0] = 0  # 第0天不持有
        for i in range(1, n):
            not_hold[i] = max(not_hold[i - 1], hold[i - 1] + prices[i])
            # 今天不持有，要么是昨天就不持有今天继续保持；要么是昨天持有，今天卖出
            if i < 2:  # 当i==1时,此时持有不可能是卖了再买的，所以此时一定是(1.昨天买的今天不变)或(2.昨天没有今天买入)
                hold[i] = max(hold[i - 1], not_hold[i - 1] - prices[i])
            else:  # i>=1时，今天持有，要么是昨天就持有今天保持；要么是前天不持有，今天买入(刚卖掉需要隔一天才能买入)
                hold[i] = max(hold[i - 1], not_hold[i - 2] - prices[i])
        return not_hold[n - 1]
class Solution2:
    def maxProfit(self, prices) -> int:
        # Solution的优化版本，将数组修改为变量
        if not prices:
            return 0
        hold = -prices[0]  # 第0天持有
        not_hold = 0
        not_hold_pre = 0  # 代表dp[i-2][0]:即前天不持有
        for i in range(1, len(prices)):
            temp = not_hold
            not_hold = max(not_hold, hold + prices[i])
            # 今天不持有，要么是昨天就不持有今天继续保持；要么是昨天持有，今天卖出
            hold = max(hold, not_hold_pre - prices[i])
            # 今天持有，要么是昨天就持有今天保持；要么是前天不持有，今天买入(刚卖掉需要隔一天才能买入)
            not_hold_pre = temp
        return not_hold
class Solution3:
    def maxProfit(self, prices) -> int:
        # labuladong的算法小抄
        dp_i_0, dp_i_1 = 0, float('-inf')
        dp_pre_0 = 0  # 代表dp[i-2][0]
        for i in range(len(prices)):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
            dp_pre_0 = temp
        return dp_i_0


if __name__ == '__main__':
    so = Solution()
    prices = [1, 2, 3, 0, 2]
    print(so.maxProfit(prices))
