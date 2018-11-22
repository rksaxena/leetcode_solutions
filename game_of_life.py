
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
    Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population..
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction
"""


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        if not board:
            return

        m = len(board)
        n = len(board[0])

        change_to_0 = set()
        change_to_1 = set()
        moves = [(-1, -1), (-1, 0), (-1, 1),
                 (0, -1), (0, 1),
                 (1, -1), (1, 0), (1, 1)
                 ]

        def valid_move(x, y):
            return x >= 0 and x < m and y >= 0 and y < n
        for i in range(m):
            for j in range(n):
                live_c = 0
                for move in moves:
                    x = i + move[0]
                    y = j + move[1]
                    if valid_move(x, y):
                        # Rule 1
                        if board[x][y] == 1:
                            live_c += 1
                if board[i][j] == 1:
                    if live_c < 2 or live_c > 3:
                        # Rule 1, 3
                        change_to_0.add((i, j))
                else:
                    if live_c == 3:
                        change_to_1.add((i, j))

        for i, j in change_to_0:
            board[i][j] = 0

        for i, j in change_to_1:
            board[i][j] = 1
