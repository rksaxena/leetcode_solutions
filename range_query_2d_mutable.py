
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.m = len(matrix)
        if not self.m:
            return
        self.n = len(matrix[0])
        self.row_sum = [[0] * self.n for _ in range(self.m+1)]

        for i in range(self.m):
            for j in range(self.n):
                self.row_sum[i+1][j] += self.row_sum[i][j] + matrix[i][j]

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        for i in range(row, self.m):
            self.row_sum[i+1][col] += diff

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
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
