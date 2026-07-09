# Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


class Solution:
    def boundaryTraversal(self,root):
        if not root:
            return []
        
        result= []
        
        def isLeaf(node):
            return node.left is None and node.right is None
        
        if not isLeaf(root):
            result.append(root.data)
        
        def addLeftBoundary(node):
            curr= node.left
            while curr:
                if not isLeaf(curr):
                    result.append(curr.data)
                if curr.left:
                    curr= curr.left
                else:
                    curr= curr.right
        
        def addLeaves(node):
            if not node:
                return
            if isLeaf(node):
                result.append(node.data)
                return
            addLeaves(node.left)
            addLeaves(node.right)
        
        def addRightBoundary(node):
            curr= node.right
            temp= []
            while curr:
                if not isLeaf(curr):
                    temp.append(curr.data)
                if curr.right:
                    curr= curr.right
                else:
                    curr= curr.left
            result.extend(reversed(temp))
        
        addLeftBoundary(root)
        addLeaves(root)
        addRightBoundary(root)
        
        return result