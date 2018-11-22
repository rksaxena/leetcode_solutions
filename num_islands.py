
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
https://leetcode.com/problems/number-of-islands/

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water
and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3

"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(x, y):
            visited[x][y] = True
            for dx, dy in moves:
                i = x + dx
                j = y + dy
                if 0 <= i < m and 0 <= j < n and grid[i][j] == "1" and not visited[i][j]:
                    dfs(i, j)

        c = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    c += 1
                    dfs(i, j)

        return c
