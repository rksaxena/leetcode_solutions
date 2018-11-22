
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.diff = float('inf')
        self.ans = root.val
        self.helper(root, target)
        return self.ans

    def helper(self, root, target):
        if root:
            d = abs(root.val - target)
            if d < self.diff:
                self.diff = d
                self.ans = root.val
                if d == 0:
                    return

            if target > root.val:
                self.helper(root.right, target)
            else:
                self.helper(root.left, target)
