
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses
"""


class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0

        min_r, min_g, min_b = 0, 0, 0
        for r, g, b in costs:
            prev_r = min_r
            prev_b = min_b
            prev_g = min_g
            min_r = r + min(prev_g, prev_b)
            min_g = g + min(prev_r, prev_b)
            min_b = b + min(prev_r, prev_g)

        return min(min_r, min_g, min_b)
