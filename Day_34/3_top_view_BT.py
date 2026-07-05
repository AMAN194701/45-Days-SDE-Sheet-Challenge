from collections import deque

class Solution:
    def topView(self, root):
        if not root:
            return []

        q = deque([(root, 0)])
        mp = {}

        while q:
            node, hd = q.popleft()

            # Store only the first node at this HD
            if hd not in mp:
                mp[hd] = node.data

            if node.left:
                q.append((node.left, hd - 1))

            if node.right:
                q.append((node.right, hd + 1))

        ans = []

        for hd in sorted(mp):
            ans.append(mp[hd])

        return ans