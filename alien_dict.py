
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
Given a sorted dictionary (array of words) of an alien language, find order of characters in the language.

"""
from collections import defaultdict

NOT_VISITED = 0
VISITING = 1
VISITED = 2


class Solution(object):
    def add_edges(self, word1, word2):
        l1 = len(word1)
        l2 = len(word2)
        n = min(l1, l2)
        for i in range(n):
            if word1[i] != word2[i]:
                self.graph[word2[i]].append(word1[i])
                break

    def topological_sort(self, ch):
        # print ch, self.visit_status
        if self.visit_status[ch] == VISITING:
            # If we visit the same node again, that signifies a cycle. Return False
            return False
        if self.visit_status[ch] == VISITED:
            return True
        self.visit_status[ch] = VISITING
        for prev_ch in self.graph[ch]:
            if not self.topological_sort(prev_ch):
                return False
        self.visit_status[ch] = VISITED
        self.ans += ch
        return True

    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        self.graph = defaultdict(list)
        self.ans = ""
        self.visit_status = {}
        for word in words:
            for ch in word:
                self.visit_status[ch] = NOT_VISITED

        n = len(words)
        for i in range(n-1):
            self.add_edges(words[i], words[i+1])
        # print self.graph

        for ch, status in self.visit_status.items():
            if status == NOT_VISITED:
                if not self.topological_sort(ch):
                    return ""

        return self.ans
