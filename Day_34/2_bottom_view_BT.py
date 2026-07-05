from queue import Queue
from collections import defaultdict

class Solution:
    def bottomView(self, root):
        result = []

        if root is None:
            return result

        mpp = defaultdict(int)

        q = Queue()
        q.put((root, 0))
        while not q.empty():
            node, line = q.get()
            # overwrite every time
            mpp[line] = node.data

            # process left child  
            if node.left:
                q.put((node.left, line - 1))
                
            # process right child
            if node.right:
                q.put((node.right, line + 1))

        for key, value in sorted(mpp.items()):
            result.append(value)

        return result
        