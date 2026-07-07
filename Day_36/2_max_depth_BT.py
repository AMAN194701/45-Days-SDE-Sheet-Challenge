class Solution:
    def maxDepth(self, root):
         # base Case
        if root is None:
            return 0

        # find height of left subtree
        left = self.maxDepth(root.left)

        # find height of right subtree
        right = self.maxDepth(root.right)

        # Return max height
        return 1 + max(left, right)
        