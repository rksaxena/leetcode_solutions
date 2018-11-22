
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

"""
from heapq import heappush, heappop


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        h = []
        n = len(lists)
        for i in range(n):
            if lists[i]:
                heappush(h, (lists[i].val, lists[i]))

        head = ListNode(0)
        tail = head

        while h:
            v = heappop(h)
            if v:
                node = v[1]
                tail.next = node
                tail = node
                if v[1].next:
                    lt = v[1].next
                    heappush(h, (lt.val, lt))

        return head.next
