class Solution:
    def rightSideView(self, root):
        result = []

        def dfs(node, level):
            # base case
            if not node:
                return
            # 1st node visit at this level
            if len(result)==level:
                result.append(node.val)

            # visit right subtree first
            dfs(node.right,level + 1)

            # thhen left subtree
            dfs(node.left, level + 1)
        dfs(root, 0)
        return result
        