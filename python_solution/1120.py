# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        res = 0
        def helper(node):
            nonlocal res
            if not node: return 0, 0
            lsum, lnum = helper(node.left)
            rsum, rnum = helper(node.right)
            tsum, tnum = lsum + rsum + node.val, lnum + rnum + 1
            res = max(res, tsum/tnum)
            return tsum, tnum
        helper(root)
        return res