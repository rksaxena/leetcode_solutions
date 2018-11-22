
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

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
