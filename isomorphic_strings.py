
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
https://leetcode.com/problems/isomorphic-strings/
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true

"""
from collections import defaultdict


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        c1 = defaultdict(int)
        c2 = defaultdict(int)
        for i, v in enumerate(s):
            if c1[v] != c2[t[i]]:
                return False
            c1[v] = i+1
            c2[t[i]] = i+1
        return True
