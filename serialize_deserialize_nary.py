
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

from collections import deque

# Definition for a Node.


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        if not root:
            return ""
        q = deque()
        q.append(root)
        out = []
        while q:
            node = q.popleft()
            val = node.val
            children = node.children
            out.append(str(val))
            out.append(str(len(children)))
            for child in children:
                q.append(child)
        print out
        return ' '.join(out)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        vals = data.split()
        # print vals
        root = Node(int(vals[0]), [])
        q = deque()
        q_len = deque()
        q.append(root)
        q_len.append(int(vals[1]))
        i = 2
        while i < len(vals):
            node = q.popleft()
            num_child = q_len.popleft()
            for j in range(num_child):
                child_node = Node(int(vals[i+j*2]), [])
                node.children.append(child_node)
                q.append(child_node)
                q_len.append(int(vals[i+j*2+1]))
            i += num_child * 2
        return root
