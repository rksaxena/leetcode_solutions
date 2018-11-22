
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

Example 1:

Input:
    2
   / \
  1   3
Output: true
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.prev = None
        return self.inorder(root)

    def inorder(self, root):
        if root:
            left = self.inorder(root.left)
            if self.prev and self.prev.val >= root.val:
                return False
            self.prev = root
            right = self.inorder(root.right)
            return left and right
        else:
            return True
