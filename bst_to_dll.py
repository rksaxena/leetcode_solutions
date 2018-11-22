
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None
        node = self.bst_to_dll(root)
        return node

    def bst_to_dll(self, root):
        if root is None:
            return None
        a_list = self.bst_to_dll(root.left)
        b_list = self.bst_to_dll(root.right)

        root.left = root
        root.right = root
        a_list = self.merge(a_list, root)
        a_list = self.merge(a_list, b_list)
        return a_list

    def merge(self, a_list, b_list):
        if a_list is None:
            return b_list
        if b_list is None:
            return a_list
        a_last = a_list.left
        b_last = b_list.left

        a_last.right = b_list
        b_list.left = a_last

        b_last.right = a_list
        a_list.left = b_last

        return a_list
