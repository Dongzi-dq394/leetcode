# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        # Solution by myself: Recursion + Binary Search (40ms: 74.57%)
        cand = [float('Inf'), None]
        def helper(node):
            if node:
                diff = abs(target-node.val)
                if diff<cand[0]:
                    cand[0], cand[1] = diff, node.val
                if node.val<=target:
                    helper(node.right)
                else:
                    helper(node.left)
        helper(root)
        return cand[1]