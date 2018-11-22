
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ln = len(nums)
        i = 1
        j = 0
        while i < ln:
            while i < ln and nums[i] == nums[j]:
                i += 1
            if i < ln:
                j += 1
                nums[j] = nums[i]
                i += 1
        return j+1
