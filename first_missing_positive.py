
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3

Example 2:

Input: [3,4,-1,1]
Output: 2
"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        nums.append(0)
        ln = len(nums)
        for i, v in enumerate(nums):
            if v < 0 or v >= ln:
                nums[i] = 0

        for i, v in enumerate(nums):
            nums[v % ln] += ln
        # print nums
        for i, v in enumerate(nums):
            if v/ln == 0:
                return i
        return ln
