
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in ascending order,
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5, 7, 7, 8, 8, 10], target = 8
Output: [3, 4]

Example 2:

Input: nums = [5, 7, 7, 8, 8, 10], target = 6
Output: [-1, -1]

"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        : type nums: List[int]
        : type target: int
        : rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        low = 0
        h = len(nums) - 1
        found = False
        while (low <= h):
            m = (low + h)/2
            if target == nums[m]:
                found = True
                break
            elif target < nums[m]:
                h = m - 1
            else:
                low = m + 1
        if not found:
            return [-1, -1]
        left = m
        right = m
        while left > 0 and nums[left-1] == nums[m]:
            left -= 1
        while right < len(nums) - 1 and nums[right+1] == nums[m]:
            right += 1
        return [left, right]
