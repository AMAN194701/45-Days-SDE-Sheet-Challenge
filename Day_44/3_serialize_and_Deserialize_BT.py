# Definition for a binary tree node.
from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return ""

        res =[]
        q=deque([root])

        while q:
            node= q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("N")
        return ",".join(res)
        
    def deserialize(self, data):
        if not data:
            return None

        values= data.split(",")
        root = TreeNode(int(values[0]))
        q = deque([root])

        i = 1
        while q:
            node= q.popleft()
            if values[i] != "N":
                node.left = TreeNode(int(values[i]))
                q.append(node.left)
            i +=1
            if values[i] != "N":
                node.right = TreeNode(int(values[i]))
                q.append(node.right)
            i += 1
        return root
