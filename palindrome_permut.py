
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
given a string check if any of its permuation is a palindrome
"""
from collections import Counter


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c = Counter(s)
        odd = 0
        for key, val in c.items():
            if val % 2 != 0:
                odd += 1
                if odd > 1:
                    return False

        return True
