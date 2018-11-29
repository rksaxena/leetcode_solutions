
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally. 
"""


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        self.grid = grid
        self.M = m
        self.N = n
        self.visited = [[False] * n for x in range(m)]
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not self.visited[i][j]:
                    area = self.maxArea(i, j)
                    max_area = max(area, max_area)
        return max_area

    def maxArea(self, i, j):
        self.visited[i][j] = True
        area = 0
        if self.isSafe(i-1, j):
            area += self.maxArea(i-1, j)

        if self.isSafe(i+1, j):
            area += self.maxArea(i+1, j)

        if self.isSafe(i, j-1):
            area += self.maxArea(i, j-1)

        if self.isSafe(i, j+1):
            area += self.maxArea(i, j+1)

        return 1 + area

    def isSafe(self, i, j):
        if i >= 0 and i < self.M and j >= 0 and j < self.N and self.grid[i][j] == 1 and not self.visited[i][j]:
            return True
