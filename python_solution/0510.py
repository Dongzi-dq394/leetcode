"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        # Solution 1: Tree (76ms: 96.74%)
        if node.right:
            res = node.right
            while res.left:
                res = res.left
            return res
        else:
            res = node
            while res.parent and res.parent.right==res:
                res = res.parent
            return None if not res.parent else res.parent