
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        out = ""
        n = len(s)
        if n <= 2 or numRows == 1:
            return s
        max_gap = 2 * (numRows-1)
        for r in range(numRows-1, -1, -1):
            i = numRows - r - 1
            if r > 0:
                gap = 2*r
            else:
                gap = 2 * (numRows-1)
            while(i < n):
                if gap == 0:
                    gap = max_gap
                out += s[i]
                i += gap
                gap = max_gap - gap
        return out
