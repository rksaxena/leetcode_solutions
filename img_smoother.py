
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:

Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
"""


class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        if not M:
            return []

        m = len(M)
        n = len(M[0])
        grey = [[0] * n for x in range(m)]
        moves = [(-1, -1), (-1, 0), (-1, 1),
                 (0, -1), (0, 1),
                 (1, -1), (1, 0), (1, 1)
                 ]

        def is_valid_move(x, y):
            return x >= 0 and x < m and y >= 0

        for i in range(m):
            for j in range(n):
                s = M[i][j]
                nn = 1
                for move in moves:
                    x = i + move[0]
                    y = j + move[1]
                    if is_valid_move(x, y):
                        nn += 1
                        s += M[x][y]
                # print s, nn
                avg = s / nn
                grey[i][j] = avg

        return grey
