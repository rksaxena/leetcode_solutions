
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
"""
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.leaf_seq(root1) == self.leaf_seq(root2)

    def leaf_seq(self, root):
        if root is None:
            return ""
        seq = ""
        s = []
        s.append(root)
        while len(s) > 0:
            node = s.pop()
            if node.left is None and node.right is None:
                seq += str(node.val)
            if node.left:
                s.append(node.left)
            if node.right:
                s.append(node.right)
        #print seq
        return seq
