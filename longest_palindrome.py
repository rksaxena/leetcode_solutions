
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
https://leetcode.com/problems/longest-palindromic-substring/
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"


"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s:
            return ""

        n = len(s)
        start = 0
        end = 0

        def expand(s, ln, r, n):
            while ln >= 0 and r < n and s[ln] == s[r]:
                ln -= 1
                r += 1
            return r - ln - 1
        for i in range(n):
            len1 = expand(s, i, i, n)
            len2 = expand(s, i, i+1, n)
            max_l = len1 if len1 > len2 else len2
            if max_l > end - start:
                end = i + max_l/2
                start = i - (max_l-1)/2

        return s[start:end+1]
