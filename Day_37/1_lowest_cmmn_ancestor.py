class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root ==p or root== q:
            return root
        # search in left subtree
        left=self.lowestCommonAncestor(root.left,p,q)

        # search in right subtree
        right=self.lowestCommonAncestor(root.right,p,q)

        # both sides found
        if left and right:
            return root

        # one side found
        return left if left else right
        