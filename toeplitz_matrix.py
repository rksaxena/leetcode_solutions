
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if not matrix:
            return False

        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r > 0 and c > 0:
                    # print matrix[r-1][c-1], matrix[r][c]
                    if matrix[r-1][c-1] != matrix[r][c]:
                        return False
        return True
