
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
Given a string, find the longest substring that contains only two unique characters. For example, given "abcbbbbcccbdddadacb", the longest substring that contains 2 unique character is "bcbbbbcccb"
"""


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        d = {}
        m, max_l = 0, 0

        for i, v in enumerate(s):
            d[v] = i
            if len(d) > k:
                m = min(d.values())
                del d[s[m]]
                m += 1

            max_l = max_l if max_l > (i - m + 1) else (i - m + 1)
        return max_l
