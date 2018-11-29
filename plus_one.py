
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        c = 1
        for i in range(n-1, -1, -1):
            if digits[i] + c < 10:
                digits[i] += c
                c = 0
                break
            else:
                s = digits[i] + c
                digits[i] = s % 10
                c = s/10

        if i == 0 and c != 0:
            digits.insert(0, c)

        return digits
