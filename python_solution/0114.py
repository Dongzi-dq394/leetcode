# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Solution 1 from hint: Use pre-order traversal (32ms: 95%)
        if not root: return
        stack = []
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
        temp = root
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            temp.left = None
            temp.right = node
            temp = temp.right
        
        # Solution 2: pre-order can be done by rotate or recursion
        # This is rotation
        # Recursion is not that simple
        while root:
            if root.left:
                temp = root.left
                while temp.right:
                    temp = temp.right
                temp.right = root.right
                root.right = root.left
                root.left = None
            root = root.right