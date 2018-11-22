
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
https://leetcode.com/problems/longest-valid-parentheses/

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        st = [-1]
        max_l = 0
        n = len(s)
        i = 0
        while i < n:
            if s[i] == '(':
            # Append the index to stack if new open parantheses
                st.append(i)
            else:
                if st:
                    st.pop()
                # print st
                if not st:
                    st.append(i)
                else:
                    max_l = max(max_l, (i - st[-1]))

            i += 1
        return max_l
