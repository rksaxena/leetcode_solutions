
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner
of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        ways = [[1] * n for x in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    ways[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        ways[i][j] = 1
                    elif i == 0 and j > 0:
                        ways[i][j] = ways[i][j-1]
                    elif j == 0 and i > 0:
                        ways[i][j] = ways[i-1][j]
                    else:
                        ways[i][j] = ways[i-1][j] + ways[i][j-1]
        return ways[m-1][n-1]
