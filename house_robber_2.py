
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.

"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        dp_with_first = [0] * n
        dp_with_last = [0] * n

        # Take first element so can't take last
        dp_with_first[0] = nums[0]
        dp_with_first[1] = nums[0]

        for i in xrange(2, n-1):
            dp_with_first[i] = dp_with_first[i-1] if dp_with_first[i-1] > dp_with_first[i-2] + \
                nums[i] else dp_with_first[i-2] + nums[i]

        # Do not take first element to take last
        dp_with_last[0] = 0
        dp_with_last[1] = nums[1]
        for i in xrange(2, n):
            dp_with_last[i] = dp_with_last[i-1] if dp_with_last[i-1] > dp_with_last[i-2] + \
                nums[i] else dp_with_last[i-2] + nums[i]

        return dp_with_first[n-2] if dp_with_first[n-2] > dp_with_last[n-1] else dp_with_last[n-1]
