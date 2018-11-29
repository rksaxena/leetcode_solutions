
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        lh = ListNode(-1)
        lt = lh
        while l1 and l2:
            if l1.val < l2.val:
                lt.next = l1
                l1 = l1.next
            else:
                lt.next = l2
                l2 = l2.next
            lt = lt.next

        lt.next = l1 or l2
        return lh.next
