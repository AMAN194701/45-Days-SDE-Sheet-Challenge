from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfsHeight(node):
            if node is None:
                return 0

            leftHeight=dfsHeight(node.left)

            if leftHeight ==-1:
                return -1

            rightHeight =dfsHeight(node.right)

            if rightHeight== -1:
                return -1

            if abs(leftHeight - rightHeight) > 1:
                return -1

            return 1 + max(leftHeight, rightHeight)

        return dfsHeight(root)!= -1
        