
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        m = len(word1)
        n = len(word2)

        if m == 0:
            return n

        if n == 0:
            return m

        m += 1
        n += 1

        dp = [[0]*n for _ in range(m)]
        dp[0] = [x for x in range(n)]
        for i in range(m):
            dp[i][0] = i
        for i in range(1, m):
            for j in range(1, n):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

        return dp[m-1][n-1]
