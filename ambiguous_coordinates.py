
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
https://leetcode.com/problems/ambiguous-coordinates/

We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)".  Then, we removed all commas, decimal points, and spaces, and ended up with the string S.  Return a list of strings representing all possibilities for what our original coordinates could have been.

Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other number that can be represented with less digits.  Also, a decimal point within a number never occurs without at least one digit occuring before it, so we never started with numbers like ".1".

The final answer list can be returned in any order.  Also note that all coordinates in the final answer have exactly one space between them (occurring after the comma.)

Example 1:
Input: "(123)"
Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]

"""


class Solution(object):
    def ambiguousCoordinates(self, s):
        """
        :type S: str
        :rtype: List[str]
        """
        if not s:
            return []
        out = []
        s = s[1:-1]
        for i in range(1, len(s)):
            num1, num2 = s[:i], s[i:]
            for x in range(len(num1)):
                if x == 0:
                    n1 = num1
                else:
                    n1 = num1[:x] + "." + num1[x:]
                if self.is_valid(n1):
                    if self.is_valid(num2):
                        out.append("({}, {})".format(n1, num2))
                    for y in range(1, len(num2)):
                        n2 = num2[:y] + "." + num2[y:]
                        if self.is_valid(n2):
                            out.append("({}, {})".format(n1, n2))
        return out

    def is_valid(self, n):
        s = n.split(".")
        if len(s) > 1 and s[1][-1] == '0':
            return False

        if len(s[0]) > 1 and s[0][0] == '0':
            return False

        return True
