# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root):
        self.maxSum = float('-inf')

        def dfs(node):
            if node is None:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            currentPath = left + right + node.val

            self.maxSum = max(self.maxSum, currentPath)

            return node.val + max(left, right)

        dfs(root)

        return self.maxSum
        