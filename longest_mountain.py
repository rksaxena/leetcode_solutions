
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

    B.length >= 3
    There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]

(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain.

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
"""


class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        max_l = -1
        i = 0
        while i < n-1:
            ln = 0
            j = i
            while (i < n - 1) and A[i+1] > A[i]:
                # Uphill
                ln += 1
                i += 1

            if j != i:
                j = i
                while (i < n-1) and A[i+1] < A[i]:
                    ln += 1
                    i += 1

                if j == i:
                    ln = 0
                    i += 1
                else:
                    max_l = max(max_l, ln)
            else:
                i += 1
        return max_l + 1
