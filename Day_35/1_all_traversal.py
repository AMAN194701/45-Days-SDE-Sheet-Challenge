# Definition for a Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def preInPostTraversal(self, root):
        # List to store traversal
        pre = []
        ino = []
        post = []

        # edge case
        if root is None:
            return [pre, ino, post]
        # Stack stores (node, state)
        stack = [(root, 1)]

        while stack:
            node, state = stack.pop()

            # Preorder
            if state == 1:
                pre.append(node.data)

                # Change state to 2 and push back
                stack.append((node, 2))

                # Traverse left subtree
                if node.left:
                    stack.append((node.left, 1))

            # Inorder
            elif state == 2:
                ino.append(node.data)

                # Change state to 3 and push back
                stack.append((node, 3))

                # Traverse right 
                if node.right:
                    stack.append((node.right, 1))

            # Postorder
            else:
                post.append(node.data)

        return [pre, ino, post]


if __name__ == "__main__":

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    sol = Solution()

    pre, ino, post = sol.preInPostTraversal(root)

    print("Preorder :", pre)
    print("Inorder  :", ino)
    print("Postorder:", post)