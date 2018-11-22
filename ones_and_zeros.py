
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

Note:

    The given numbers of 0s and 1s will both not exceed 100
    The size of given string array won't exceed 600.

Example 1:

Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4
"""


class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        if not strs:
            return 0
        size = len(strs)
        dp = [[[0] * (n+1) for y in range(m+1)] for x in range(size+1)]

        for i in range(1, size+1):
            zeros = strs[i-1].count('0')
            ones = len(strs[i-1]) - zeros
            for zi in range(m+1):
                for oi in range(n+1):
                    taken = -1
                    if zi >= zeros and oi >= ones:
                        taken = dp[i-1][zi - zeros][oi-ones] + 1

                    dp[i][zi][oi] = max(dp[i-1][zi][oi], taken)

        return dp[size][m][n]
