
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        right = len(height) - 1
        if right < 0:
            return 0
        left = 0
        water = 0
        while(left < right):
            if height[left] < height[right]:
                c = 1
                while height[left] > height[left+c]:
                    water += height[left] - height[left+c]
                    c += 1
                left += c
            else:
                c = 1
                while height[right] > height[right - c]:
                    water += height[right] - height[right - c]
                    c += 1
                right -= c
        return water
