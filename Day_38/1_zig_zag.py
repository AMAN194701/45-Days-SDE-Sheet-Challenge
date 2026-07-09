# Definition for a binary tree node.

from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root ):
        if not root:
            return []

        result= []
        q= deque([root])
        lt_to_rt=True

        while q:
            size= len(q)
            level= deque()

            for _ in range(size):
                node= q.popleft()

                if lt_to_rt:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            result.append(list(level))
            lt_to_rt= not lt_to_rt

        return result
        