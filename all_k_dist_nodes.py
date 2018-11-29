
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.



Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation:
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.

"""
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        self.dist_map = {}
        self.output = []
        self.update_dist(root, target)
        self.preorder(root, target, K, self.dist_map[root])
        return self.output

    def update_dist(self, root, target):
        if root is None:
            return -1

        if root == target:
            self.dist_map[root] = 0
            return 0

        left = self.update_dist(root.left, target)
        if left >= 0:
            self.dist_map[root] = left + 1
            return left + 1

        right = self.update_dist(root.right, target)
        if right >= 0:
            self.dist_map[root] = right + 1
            return right + 1

        return -1

    def preorder(self, root, target, K, dist):
        if root is None:
            return

        if root in self.dist_map:
            dist = self.dist_map[root]

        if dist == K:
            self.output.append(root.val)

        self.preorder(root.left, target, K, dist+1)
        self.preorder(root.right, target, K, dist+1)
