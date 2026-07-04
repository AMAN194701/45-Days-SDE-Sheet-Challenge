class Solution:
    def preorderTraversal(self, root):
        stack = []
        ans = []
        current = root
        while current or stack:
            # Move left as possible
            while current:
                ans.append(current.val)      
                stack.append(current)
                current = current.left
            current = stack.pop()
            current = current.right

        return ans
        