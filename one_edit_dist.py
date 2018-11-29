
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
Given two strings S and T, determine if they are both one edit distance apart.
"""


class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l1 = len(s)
        l2 = len(t)

        if not l1 and not l2:
            return False

        if abs(l1 - l2) > 1:
            return False

        if l2 > l1:
            s, t = t, s
            l1, l2 = l2, l1

        if l1 == l2:
            diff = 0
            for i in range(l1):
                if s[i] != t[i]:
                    diff += 1
            if diff == 0 or diff > 1:
                return False

        else:
            i = 0
            j = 0
            diff = 0
            while i < l1 and j < l2:
                if s[i] != t[j]:
                    diff += 1
                    i += 1
                else:
                    i += 1
                    j += 1
                if diff > 1:
                    return False
            if i != l1 and j != l2:
                return False

        return True
