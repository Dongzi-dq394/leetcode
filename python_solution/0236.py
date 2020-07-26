# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None
        if root == p or root == q: return root
        node1 = self.lowestCommonAncestor(root.left, p, q)
        node2 = self.lowestCommonAncestor(root.right, p, q)
        if node1 and node2: return root
        return node1 if node1 else node2