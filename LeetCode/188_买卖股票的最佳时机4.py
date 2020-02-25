# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/2/24 12:09
class Solution:
    def maxProfit(self, k, prices) -> int:
        return self.max_profit_k(prices, k)

    def max_profit_inf(self, prices):
        # 当k>=n/2(总天数的一半)，此时k可以理解为最大交易次数没有限制，
        # 此时k不会影响到profit，此时题目退化为[122_买卖股票的最佳时机2]
        # k=n/2的意思是，今天买，明天卖，后天再买入，大后天再卖出，一替一天的操作
        n = len(prices)
        hold = -prices[0]
        not_hold = 0
        for i in range(1, n):
            prev_hold = hold
            hold = max(hold, not_hold - prices[i])
            not_hold = max(not_hold, prev_hold + prices[i])
        return not_hold

    def max_profit_k(self, prices, k):  # 最大交易次数为k时所获得的profit
        n = len(prices)
        if n == 0 or k == 0:
            return 0  # 当n=0(天数为0时)，或者k=0(没有交易次数，无法交易)时
        if k >= n / 2:  # 此时题目退化为[122_买卖股票的最佳时机2]
            return self.max_profit_inf(prices)

        # hold和not_hold分别表示当前[持有]或[不持有]时的profit
        hold = [[0 for i in range(k + 1)] for j in range(n)]  # 当前持有shape([n*(k+1)])
        not_hold = [[0 for i in range(k + 1)] for j in range(n)]  # 当前不持有 shape([n*(k+1)])

        for i in range(n):  # 天数
            for j in range(1, k + 1):  # 交易次数k(可以理解为剩余交易次数)
                if i == 0:  # base case
                    hold[i][j] = -prices[i]  # 天数为0的时候，持有，则买入花了-prices[i]的钱
                    not_hold[i][j] = 0  # 天数为0的时候，不持有，profit为0
                else:
                    not_hold[i][j] = max(not_hold[i - 1][j], hold[i - 1][j] + prices[i])
                    # 当i不是第0天时，此时not_hold为max([昨天未持有，今天仍未持有],[昨天持有，今天卖出并收入prices[i]])
                    if j == 1:  # 当j=1时只能进行一次交易[买入和卖出一支股票]
                        hold[i][j] = max(hold[i - 1][j], 0 - prices[i])
                        # 在只有一次交易的情况下持有，说明要么是昨天持有剩下来的(该次交易次数没有被用掉)，
                        # 要么是原来不持有(profit为0)，并且把交易次数在这次用掉，花掉prices[i]的钱，变成[持有]状态
                    else:
                        hold[i][j] = max(hold[i - 1][j], not_hold[i - 1][j - 1] - prices[i])
                        # 交易次数不为1的情况下持有，说明要么是昨天持有剩下来的(在没有卖出之前说明此次交易未结束，所以j不变)
                        # 要么是昨天没有持有，今天买入(我们记买入是一次交易的开始，卖出才是这次交易的结束)，其中昨天没有持有
                        # 说明上次交易已经结束(卖掉了)，所以昨天的not_hold状态是[j-1]
        return not_hold[n - 1][k]


if __name__ == '__main__':
    so = Solution()
    prices = [3, 2, 6, 5, 0, 3]
    k = 2
    print(so.maxProfit(k, prices))
