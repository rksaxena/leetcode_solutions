
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

"""
# Definition for an interval.


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        n = len(intervals)
        if not n:
            return []
        intervals.sort(key=(lambda x: x.start))
        ans = []
        i = 0
        while i < n:
            start = intervals[i].start
            end = intervals[i].end
            while i < n - 1 and end >= intervals[i+1].start:
                end = max(end, intervals[i+1].end)
                i += 1
            ans.append(Interval(start, end))
            i += 1
        return ans
