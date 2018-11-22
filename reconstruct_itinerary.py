
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
https://leetcode.com/problems/reconstruct-itinerary/

Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
"""
from collections import defaultdict


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """

        if not tickets:
            return []

        trips = defaultdict(list)
        for t in tickets:
            trips[t[0]].append(t[1])

        for trip in trips:
            trips[trip].sort()

        start = 'JFK'
        it = []

        def dfs(at):
            #print at
            while trips[at]:
                to = trips[at].pop(0)
                dfs(to)
            it.append(at)

        dfs(start)
        return it[::-1]
