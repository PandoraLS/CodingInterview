# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/2/24 17:31

class Solution:
    def maxProfit(self, prices) -> int:
        # 动态规划
        if not prices:
            return 0
        left_min = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            left_min = min(prices[i], left_min)
            if prices[i] - left_min > profit:
                profit = prices[i] - left_min
        return profit
    
class Solution2:
    def maxProfit(self, prices) -> int:
        # labuladong的算法小抄
        dp_i_0, dp_i_1 = 0, float('-inf')
        for i in range(len(prices)):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, -prices[i])
        return dp_i_0

if __name__ == '__main__':
    so = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(so.maxProfit(prices))
    
    so2 = Solution2()
    print(so2.maxProfit(prices))
