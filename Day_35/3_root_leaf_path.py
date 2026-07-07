class Solution:
    def binaryTreePaths(self, root):
        ans = []
        def dfs(node, path):
            if node is None:
                return

            # add current node to the path
            path.append(str(node.val))

            # if it is a leaf node
            if node.left is None and node.right is None:
                ans.append("->".join(path))
            else:
                dfs(node.left, path)
                dfs(node.right, path)

            # backtrack
            path.pop()
        dfs(root, [])
        
        return ans