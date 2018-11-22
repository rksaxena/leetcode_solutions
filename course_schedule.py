
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

from collections import defaultdict

NOT_VISITED = 0
VISITING = 1
VISITED = 2


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not numCourses:
            return True

        g = Graph(numCourses)
        for p in prerequisites:
            g.add_edge(p[1], p[0])

        return not g.is_cyclic()


class Graph:
    def __init__(self, v):
        self.graph = defaultdict(list)
        self.v = v

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_cyclic_util(self, v, visited):

        if visited[v] == VISITING:
            return True
        visited[v] = VISITING

        # Recur for all neighbours
        # if any neighbour is visited and in
        # recStack then graph is cyclic
        for neighbour in self.graph[v]:
            if self.is_cyclic_util(neighbour, visited):
                return True

        visited[v] = VISITED
        return False

    def is_cyclic(self):
        visited = [0] * self.v
        for node in range(self.v):
            if visited[node] == NOT_VISITED:
                if self.is_cyclic_util(node, visited):
                    return True
        return False
