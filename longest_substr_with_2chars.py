
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
Given a string, find the longest substring with atmost two chars
"""


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        curr_len = 0
        first = second = s[0]
        end_of_second = 0
        ans = 0

        for c in s:
            if c == second:
                # Continue to grow the substring with second character
                curr_len += 1
                end_of_second += 1
            elif c == first:
                # New char is the first character of the substring so:
                # 1. Increase the curr_len of substring
                # 2. Mark the first char as second and second as first
                # 3. Mark the end of second character as it is the first occurence after second char
                curr_len += 1
                first, second = second, first
                end_of_second = 1
            else:
                # For New char:
                # 1. Mark the new char as second and second char as first
                # 2. Check the curr_len against total max_len
                # 3. Mark the end of second character
                first = second
                second = c
                ans = curr_len if curr_len > ans else ans
                curr_len = end_of_second + 1
                end_of_second = 1

        return curr_len if curr_len > ans else ans
