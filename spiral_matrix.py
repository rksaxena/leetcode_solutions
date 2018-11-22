
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])

        start_i = start_j = 0
        end_i = m
        end_j = n
        out = []
        i = start_i
        j = start_j
        while start_i < end_i and start_j < end_j:

            j = start_j
            # Right
            while j < end_j:
                # print "Right"
                out.append(matrix[i][j])
                j += 1

            j -= 1
            start_i += 1
            i = start_i
            # Down
            while i < end_i:
                # print "Down"
                out.append(matrix[i][j])
                i += 1

            end_j -= 1
            j = end_j - 1
            i -= 1
            # Left
            if start_i < end_i:
                while j >= start_j:
                    # print "Left"
                    out.append(matrix[i][j])
                    j -= 1

                end_i -= 1
                j += 1

            # Up
            i = end_i - 1
            if start_j < end_j:
                while i >= start_i:
                    # print "Up"
                    out.append(matrix[i][j])
                    i -= 1
                start_j += 1
                i += 1

        return out
