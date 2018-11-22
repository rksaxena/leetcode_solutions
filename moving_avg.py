
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
"""
from collections import deque


class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.n = size
        self.sum = 0
        self.q = deque()
        self.count = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.sum += val
        self.q.append(val)
        if self.count < self.n:
            self.count += 1
        else:
            self.sum -= self.q.popleft()

        return float(self.sum)/float(self.count)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
