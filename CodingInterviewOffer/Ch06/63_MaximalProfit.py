# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/1/10 19:38

"""
题目：https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
题解：https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39049/Easy-O(n)-Python-solution
因为它通过比较到目前为止的最低价格来重新计算每次迭代的利润，它确实确保【先购买，后卖出】的要求。
"""


class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        min_price_so_far = float('inf')

        for current_price in prices:
            min_price_so_far = min(current_price, min_price_so_far)
            best_possible_profit_if_sold_now = current_price - min_price_so_far
            max_profit = max(best_possible_profit_if_sold_now, max_profit)
        return max_profit
