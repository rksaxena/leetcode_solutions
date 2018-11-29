
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.

For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2). The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. So return 7.
"""
from collections import deque


class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        self.m = len(grid)
        self.n = len(grid[0])
        self.grid = grid
        self.dist = [[0] * self.n for x in range(self.m)]
        self.buildings = sum(val for line in grid for val in line if val == 1)
        self.reach = [[0] * self.n for x in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    if self.bfs(i, j, 0) == False:
                        return -1
        # print self.dist
        min_dist = float('inf')
        for i in range(self.m):
            for j in range(self.n):
                if self.reach[i][j] == self.buildings and self.dist[i][j] < min_dist:
                    min_dist = self.dist[i][j]
        return min_dist if min_dist != float('inf') else -1

    def bfs(self, i, j, dist):
        visited = [[False] * self.n for x in range(self.m)]
        q = deque()
        q.append((i, j, dist))
        visited[i][j] = True
        cb = 1
        while q:
            x, y, dist = q.popleft()
            for dx, dy in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if dx >= 0 and dx < self.m and dy >= 0 and dy < self.n and not visited[dx][dy]:
                    visited[dx][dy] = True
                    if self.grid[dx][dy] == 0:
                        self.dist[dx][dy] += dist + 1
                        self.reach[dx][dy] += 1
                        q.append((dx, dy, dist+1))
                    elif self.grid[dx][dy] == 1:
                        cb += 1

        return cb == self.buildings
