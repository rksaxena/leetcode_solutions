
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.

Rules for a valid pattern:

    1. Each pattern must connect at least m keys and at most n keys.
    2. All the keys must be distinct.
    3. If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
    4. The order of keys used matters.
"""

class Solution(object):
    def __init__(self):
        self.skip = {}
        self.skip[(1, 9)] = self.skip[(9, 1)] = 5
        self.skip[(2, 8)] = self.skip[(8, 2)] = 5
        self.skip[(3, 7)] = self.skip[(7, 3)] = 5
        self.skip[(4, 6)] = self.skip[(6, 4)] = 5

        self.skip[(1, 3)] = self.skip[(3, 1)] = 2
        self.skip[(1, 7)] = self.skip[(7, 1)] = 4
        self.skip[(3, 9)] = self.skip[(9, 3)] = 6
        self.skip[(7, 9)] = self.skip[(9, 7)] = 8

    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        def DFS(visited, x, ln):
            if ln < 0:
                return 0
            if ln == 0:
                return 1

            visited[x] = True
            count = 0
            for i in range(1, 10):
                if not visited[i] and ((x, i) not in self.skip or visited[self.skip[(x, i)]]):
                    count += DFS(visited, i, ln - 1)

            visited[x] = False
            return count

        result = 0
        visited = [False] * 10
        for c in range(m, n+1):
            result += DFS(visited, 1, c-1) * 4
            result += DFS(visited, 2, c-1) * 4
            result += DFS(visited, 5, c-1)

        return result
