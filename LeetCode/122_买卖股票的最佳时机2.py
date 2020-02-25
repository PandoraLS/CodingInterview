# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/2/24 18:07


class Solution:
    def maxProfit(self, prices) -> int:
        # 
        if not prices:
            return 0
        hold = -prices[0]  # 第一天持有（因为买入）
        not_hold = 0
        for i in range(1, len(prices)):
            prev_hold = hold
            hold = max(hold, not_hold - prices[i]) # 持有
            not_hold = max(not_hold, prev_hold + prices[i]) # 不持有
        return not_hold

class Solution2:
    def maxProfit(self, prices) -> int:
        # labuladong的算法小抄
        dp_i_0, dp_i_1 = 0, float('-inf')
        for i in range(len(prices)):
            old_dp_i_0, old_dp_i_1 = dp_i_0, dp_i_1
            dp_i_0 = max(old_dp_i_0, old_dp_i_1 + prices[i])
            dp_i_1 = max(old_dp_i_1, old_dp_i_0 - prices[i])
        return dp_i_0

if __name__ == '__main__':
    so = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(so.maxProfit(prices))

    so2 = Solution2()
    print(so2.maxProfit(prices)) 
