
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
https://leetcode.com/problems/fruit-into-baskets/

In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

    Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
    Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.

Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?
"""


class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        if not tree:
            return 0

        end = 0
        total = 0
        first = second = tree[0]
        ans = 0

        for fruit in tree:
            if fruit == second:
                total += 1
                end += 1
            elif fruit == first:
                total += 1
                first, second = second, first
                end = 1
            else:
                first = second
                second = fruit
                ans = total if total > ans else ans
                total = end + 1
                end = 1

        return total if total > ans else ans
