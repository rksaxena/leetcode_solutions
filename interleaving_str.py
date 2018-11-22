
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
https://leetcode.com/problems/interleaving-string/

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

"""


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        m = len(s1)
        n = len(s2)

        dp = [[False] * (n+1) for x in range(m+1)]
        dp[0][0] = True
        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]

        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = ((s1[i-1] == s3[i+j-1] and dp[i-1][j])
                            or (s2[j-1] == s3[i+j-1] and dp[i][j-1]))

        return dp[m][n]
