# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = [-float('Inf')]
        def getMaxHeight(root):
            if not root: return 0
            left_h = getMaxHeight(root.left)
            right_h = getMaxHeight(root.right)
            res.append(max(root.val, root.val+left_h, root.val+right_h, root.val+left_h+right_h))
            return max(root.val, root.val+left_h, root.val+right_h)
        getMaxHeight(root)
        return max(res)