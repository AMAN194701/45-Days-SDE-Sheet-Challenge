class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def findpredSuc(self, root, key):
        pred = None
        succ = None

        curr = root

        while curr:
            if curr.data< key:
                pred= curr
                curr = curr.right
            else:
                curr = curr.left

        curr = root
        while curr:
            if curr.data >key:
                succ = curr
                curr= curr.left
            else:
                curr= curr.right
        return [pred, succ]
        