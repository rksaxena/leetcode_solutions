
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com
"""
There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days. In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.

Given an array flowers consists of number from 1 to N. Each number in the array represents the place where the flower will open in that day.

For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x, where i and x will be in the range from 1 to N.

Also given an integer k, you need to output in which day there exists two flowers in the status of blooming, and also the number of flowers between them is k and these flowers are not blooming.

If there isn't such day, output -1.
"""
class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        if not flowers:
            return -1
        ln = len(flowers)
        bloom = [False] * ln

        for i, f in enumerate(flowers):
            curr = f - 1
            bloom[curr] = True
            # print bloom

            if i > 0:
                if (curr - k - 1 >= 0) and bloom[curr - k - 1] and not self.isBlooming(curr-k, curr, bloom):
                    return i + 1
                if (curr + k + 1 < ln) and bloom[curr + k + 1] and not self.isBlooming(curr+1, curr+k+1, bloom):
                    return i + 1

        return -1

    def isBlooming(self, start, end, bloom):
        # print bloom, start, end
        while start < end:
            if bloom[start]:
                return True
            start += 1
        return False
