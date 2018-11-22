
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
https://leetcode.com/problems/number-of-islands-ii/

A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

"""


class Solution(object):
    def __init__(self):
        self.curr_col = 1
        self.islands = {}
        self.moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        if m == 0 or n == 0:
            return []

        self.m = m
        self.n = n
        num_islands = []
        self.water = [[0] * n for _ in range(m)]
        for x, y in positions:
            neighbour_colors = self.get_neighbour_colors(x, y)
            if neighbour_colors:
                lowest_color = min(neighbour_colors)
                for c in neighbour_colors:
                    # print self.islands[c], c, neighbour_colors
                    if c and c != lowest_color:
                        self.color_neighbours(c, lowest_color)
                        del self.islands[c]

                self.water[x][y] = lowest_color
                self.islands[lowest_color].append((x, y))
                self.curr_col += 1

            else:
                self.water[x][y] = self.curr_col
                self.islands[self.curr_col] = [(x, y)]
                self.curr_col += 1

            num_islands.append(len(self.islands))
        return num_islands

    def get_neighbour_colors(self, x, y):
        nb = set()
        for dx, dy in self.moves:
            i = x + dx
            j = y + dy
            if 0 <= i < self.m and 0 <= j < self.n and self.water[i][j] > 0:
                nb.add(self.water[x + dx][y + dy])
        return nb

    def color_neighbours(self, sc, dc):
        for x, y in self.islands[sc]:
            self.water[x][y] = dc
            self.islands[dc].append((x, y))
            # print self.islands[dc]
