class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []

        stack= []
        ans= []
        lastVisited= None
        curr = root

        while stack or curr:
            if curr:
                stack.append(curr)
                curr= curr.left
            else:
                peek= stack[-1]

                if peek.right and lastVisited != peek.right:
                    curr = peek.right
                else:
                    ans.append(peek.val)
                    lastVisited= stack.pop()
        return ans