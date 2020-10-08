# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        # Solution by myself: Recursion and Merge (32ms: 56.19%)
        if not root: return []
        left = self.findLeaves(root.left)
        right = self.findLeaves(root.right)
        if len(left)<len(right):
            for i in range(len(left)):
                right[i] += left[i]
            res = right + [[root.val]]
        else:
            for i in range(len(right)):
                left[i] += right[i]
            res = left + [[root.val]]
        return res