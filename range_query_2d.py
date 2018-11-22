
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
https://leetcode.com/problems/range-sum-query-2d-immutable/

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:

Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
"""


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        #self.matrix = matrix
        m = len(matrix)
        if not m:
            return
        n = len(matrix[0])
        row_sum = [[0] * n for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                row_sum[i+1][j] += row_sum[i][j] + matrix[i][j]

        self.row_sum = row_sum

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        s = 0
        for col in range(col1, col2+1):
            s += (self.row_sum[row2+1][col] - self.row_sum[row1][col])
        return s


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
