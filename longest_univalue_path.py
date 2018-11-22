
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5

Output:

2
"""
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.max = 0
        self.findLen(root)
        return self.max

    def findLen(self, root):
        if root is None:
            return 0
        left_len = self.findLen(root.left)
        right_len = self.findLen(root.right)
        max_left = 0
        max_right = 0
        if root.left and root.left.val == root.val:
            max_left = left_len + 1

        if root.right and root.right.val == root.val:
            # include right node
            max_right = right_len + 1

        self.max = max(self.max, max_left + max_right)

        return max(max_left, max_right)
