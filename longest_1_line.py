
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

from collections import Counter
class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        rows = len(M)
        if rows == 0:
            return 0
        cols = len(M[0])
        
        h = [0] * cols
        v = [0] * rows
        d = [0] * (rows + cols - 1)
        a = [0] * (rows + cols - 1)
        max_ones = 0
        for i in range(rows):
            for j in range(cols):
                if M[i][j] == 1:
                    h[j] += 1
                    v[i] += 1
                    d[i-j] += 1
                    a[i+j] += 1
                    max_ones = max(max_ones, h[j], v[i], d[i-j], a[i+j])
                else:
                    h[j] = 0
                    v[i] = 0
                    d[i-j] = 0
                    a[i+j] = 0
                    
        return max_ones
