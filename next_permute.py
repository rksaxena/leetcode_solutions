
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return
        i = n-1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1

        # find next bigger starting number
        if i > 0:
            j = n - 1
            while j > i-1:
                if nums[j] > nums[i-1]:
                    nums[j], nums[i-1] = nums[i-1], nums[j]
                    break
                j -= 1

        # numbers from i to n are in descending order, reverse them
        start = i
        end = n - 1
        while end > start:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
