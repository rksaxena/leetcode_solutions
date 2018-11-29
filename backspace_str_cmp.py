
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
"""


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s = []
        t = []
        for c in S:
            if c == '#':
                if len(s) > 0:
                    s.pop()
            else:
                s.append(c)

        for c in T:
            if c == '#':
                if len(t) > 0:
                    t.pop()
            else:
                t.append(c)

        return t == s
