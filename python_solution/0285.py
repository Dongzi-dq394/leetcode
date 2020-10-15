# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        # Solution 1: Recursion (68ms: 92.83%)
        cand = [None]
        def helper(node):
            if node:
                if node.val>p.val:
                    cand[0] = node
                    helper(node.left)
                else:
                    helper(node.right)
        helper(root)
        return cand[0]