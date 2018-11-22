
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
https://leetcode.com/problems/bus-routes/
We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever.
For example if routes[0] =  [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.

We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.

Example:
Input:
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
Output: 2
Explanation:
The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
"""

from collections import deque
from collections import defaultdict


class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T:
            return 0

        to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for j in route:
                to_routes[j].add(i)

        q = deque()
        q.append([S, 0])
        seen = set()
        seen.add(S)

        while q:
            stop, num_bus = q.popleft()
            if stop == T:
                return num_bus
            for route_i in to_routes[stop]:
                for next_stop in routes[route_i]:
                    if next_stop not in seen:
                        q.append([next_stop, num_bus+1])
                        seen.add(next_stop)
                routes[route_i] = []

        return -1
