
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down)self.
Find all strobogrammatic numbers that are of length = n.
"""


class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.helper(n, n)

    def helper(self, i, n):
        if i == 0:
            return [""]
        if i == 1:
            return ["1", "8", "0"]

        out = []
        pivots = self.helper(i-2, n)
        for pivot in pivots:
            if i != n:
                out.append("0" + pivot + "0")
            out.append("1" + pivot + "1")
            out.append("8" + pivot + "8")
            out.append("6" + pivot + "9")
            out.append("9" + pivot + "6")

        return out
