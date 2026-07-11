# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root):
            # base case
            if root is None:
                return 0

            # height of left subtree
            lh = self.maxDepth(root.left)

            # Height of right subtree
            rh = self.maxDepth(root.right)

            # return maximum height
            return 1 + max(lh, rh)


            