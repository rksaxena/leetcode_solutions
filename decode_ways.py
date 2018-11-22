
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
"""


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0

        n = len(s) + 1
        count = [0] * n
        count[0] = 1
        count[1] = 1

        for i in range(2, n):
            if s[i-1] > '0':
                count[i] = count[i-1]

            if s[i-2] == '1' or (s[i-2] == '2' and s[i-1] < '7'):
                count[i] += count[i-2]

        return count[-1]
