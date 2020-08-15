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
        # Solution 1: BFS with stack (68ms: 71.01%)
        if not root: return root
        stack = [root]
        while stack:
            length = len(stack)
            for i in range(length-1):
                node = stack.pop(0)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                node.next = stack[0]
            node = stack.pop(0)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root
        
        # New Solution: More simple recursion (52ms: 99.58%)
        # Very smart!
        if not root: return root
        if root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)
        return root