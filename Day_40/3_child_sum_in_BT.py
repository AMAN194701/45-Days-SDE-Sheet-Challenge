class Solution:
    def checkChildrenSum(self, root):
        if root is None:
            return True

        # Leaf node always satisfies the property
        if root.left is None and root.right is None:
            return True

        left = 0
        right = 0

        if root.left:
            left = root.left.val

        if root.right:
            right = root.right.val

        return (root.val == left + right and
                self.checkChildrenSum(root.left) and
                self.checkChildrenSum(root.right))