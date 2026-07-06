from collections import defaultdict, deque
'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def verticalOrder(self, root): 
        # check if tree is empty
        if root is None:
            return []
        # Dict to store node column-wise
        column_map = defaultdict(list)

        # Queue stores (node, horiz._dis))
        queue = deque()
        queue.append((root, 0))

        while queue:
            node, hd = queue.popleft()

            # store node value in its colmn
            column_map[hd].append(node.data)

            # Left child
            if node.left:
                queue.append((node.left, hd - 1))

            # Right child 
            if node.right:
                queue.append((node.right, hd + 1))

        # Collect result from leftmost column to rightmost
        result = []

        for hd in sorted(column_map.keys()):
            result.append(column_map[hd])
        
        return result