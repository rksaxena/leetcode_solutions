
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction(i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

"""


class Solution(object):
    def maxProfit(self, prices):
        """
        : type prices: List[int]
        : rtype: int
        """
        if len(prices) < 2:
            return 0
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                p = price - min_price
                max_profit = max_profit if p < max_profit else p
        return max_profit
