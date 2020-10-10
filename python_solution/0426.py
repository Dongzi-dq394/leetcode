"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # Solution by myself: Recursion? (32ms: 89.38%)
        def helper(node):
            if not node: return None, None
            ls, le = helper(node.left)
            rs, re = helper(node.right)
            temp = Node(node.val)
            if le:
                le.right = temp
                temp.left = le
            if rs:
                rs.left = temp
                temp.right = rs
            left = ls if ls else temp
            right = re if re else temp
            return left, right
        s, e = helper(root)
        if not s: return None
        s.left = e
        e.right = s
        return s