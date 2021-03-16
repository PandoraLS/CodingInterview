"""
说明：
[123_买卖股票的最佳时机3]与[188_买卖股票的最佳时机4]的做法非常类似，两题都属于[困难]，目前只需要知道思路和需要注意的点就ok了
"""

"""
力扣121 买卖股票的最佳时机
121_买卖股票的最佳时机
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。
示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0
代码提交链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 力扣121 买卖股票的最佳时机
        if not prices:
            return 0
        n = len(prices)

        not_hold = [0 for _ in range(n)]
        hold = [0 for _ in range(n)]
        not_hold[0] = 0
        hold[0] = -prices[0]
        for i in range(1, n):
            hold[i] = max(hold[i-1], -prices[i])
            # 这里不能写成hold[i] = max(hold[i-1], not_hold[i-1]-prices[i]),
            # 因为最多买一次,这次一定是第一次,之前一定没有出现过交易,not_hold[i-1]-prices[i]指的是出现多次交易的情况
            not_hold[i] = max(not_hold[i-1], hold[i-1]+prices[i])
        return not_hold[n-1]

"""
122. 买卖股票的最佳时机 II
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
示例 1:
输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
示例 2:
输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
代码提交链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
"""

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        hold = [0 for _ in range(n)]
        not_hold = [0 for _ in range(n)]
        hold[0] = -prices[0]
        not_hold[0] = 0
        for i in range(1, n):
            not_hold[i] = max(not_hold[i-1], hold[i-1]+prices[i])
            hold[i] = max(hold[i-1], not_hold[i-1]-prices[i]) # 因为可以多次购买,这一行与121题有所不同
        return not_hold[n-1]



"""
309. 最佳买卖股票时机含冷冻期
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3 
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        not_hold = [0 for _ in range(n)]
        hold = [0 for _ in range(n)]
        hold[0] = -prices[0]  # 第0天持有说明钱花了出去
        for i in range(1, n):
            not_hold[i] = max(not_hold[i - 1], hold[i - 1] + prices[i])
            # 今天没有，要么昨天就没有，要么昨天有，今天卖了
            if i < 2:
                hold[i] = max(hold[i - 1], not_hold[i - 1] - prices[i])
                # 第1天如果有，要么第0天就有继续保持，要么第0天没有，今天买入
            else:
                # 第2天起，hold要么昨天持有今天继续保持，要么前天卖出，今天买入
                hold[i] = max(hold[i - 1], not_hold[i - 2] - prices[i])
        return not_hold[n - 1]


"""
714. 买卖股票的最佳时机含手续费
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
返回获得利润的最大值。
注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。
示例 1:

输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:  
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
注意:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution4:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        n = len(prices)
        not_hold = [0 for _ in range(n)]
        hold = [0 for _ in range(n)]
        hold[0] = -prices[0]
        for i in range(1, n):
            not_hold[i] = max(not_hold[i-1], hold[i-1]+prices[i]-fee)
            hold[i] = max(hold[i-1], not_hold[i-1]-prices[i])
        return not_hold[n-1]

"""
123_买卖股票的最佳时机3
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
示例 1:
输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2:
输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。 注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:
输入: [7,6,4,3,1] 
输出: 0 
解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。


188_买卖股票的最佳时机4
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
示例 1:
输入: [2,4,1], k = 2
输出: 2
解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2:
输入: [3,2,6,5,0,3], k = 2
输出: 7
解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。

[123_买卖股票的最佳时机3]与[188_买卖股票的最佳时机4]的做法非常类似
"""

class Solution5:
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
            for j in range(1, k + 1):  # 交易次数k(可以理解为已经交易了多少次(从1开始))
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
                        # 要么是昨天没有持有，此时就是上一次的交易完成状态了(我们记买入是一次交易的开始，卖出才是这次交易的结束)，其中昨天没有持有
                        # 说明上次交易已经结束(卖掉了)，所以昨天的not_hold状态是[j-1]
        return not_hold[n - 1][k]
