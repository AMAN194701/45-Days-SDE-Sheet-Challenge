class Solution:
    def inorderTraversal(self, root):
        ans =[]
        current =root
        while current:
            if current.left is None:
                ans.append(current.val)
                current=current.right
            else:
                # find inorder 
                predecessor=current.left

                while predecessor.right and predecessor.right!=current:
                    predecessor=predecessor.right

                # Create thread
                if predecessor.right is None:
                    predecessor.right=current
                    current = current.left
                # Thread already exist
                else:
                    predecessor.right=None
                    ans.append(current.val)
                    current=current.right

        return ans
        