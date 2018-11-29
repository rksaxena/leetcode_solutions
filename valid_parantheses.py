
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        n = len(s)
        if n % 2 != 0:
            return False
        st = []
        for i, v in enumerate(s):
            if v in "({[":
                st.append(v)
                continue
            elif len(st) == 0:
                return False
            elif v == ')' and st[-1] != '(':
                return False
            elif v == '}' and st[-1] != '{':
                return False
            elif v == ']' and st[-1] != '[':
                return False
            st.pop()
        return len(st) == 0
