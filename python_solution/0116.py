"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        stack = [root]
        while stack:
            l = len(stack)
            for i in range(l-1):
                stack[i].next = stack[i+1]
            for i in range(l):
                node = stack.pop(0)
                if node.left:
                    stack.append(node.left)
                    stack.append(node.right)
        return root