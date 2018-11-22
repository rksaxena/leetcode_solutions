
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").
"""


"""
Let n be the answer, the minimum number of times A has to be repeated.

For B to be inside A, A has to be repeated sufficient times such that it is at least as long as B (or one more), hence we can conclude that the theoretical lower bound for the answer would be length of B / length of A.

Let x be the theoretical lower bound, which is ceil(len(B)/len(A)).

The answer n can only be x or x + 1 (in the case where len(B) is a multiple of len(A) like in A = "abcd" and B = "cdabcdab") and not more. Because if B is already in A * n, B is definitely in A * (n + 1).

Hence we only need to check whether B in A * x or B in A * (x + 1), and if both are not possible return -1.
"""


class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if any(b not in set(A) for b in set(B)):
            return -1
        """
        times = int(math.ceil(float(len(B)) / len(A))) can be written as times = -(-len(B) // len(A))
        """
        times = -(-(len(B))/len(A))
        if B in (A*times):
            return times
        elif B in (A*(times+1)):
            return times+1
        return -1
