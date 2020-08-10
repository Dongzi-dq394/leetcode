# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        # Solution 1: Recursion (60ms: 80.51%)
        # Recursion part can be memorized by DP array!
        def getNodes(nums):
            if not nums: return [None]
            res = []
            for i, num in enumerate(nums):
                left_tree = getNodes(nums[:i])
                right_tree = getNodes(nums[i+1:])
                for l in left_tree:
                    for r in right_tree:
                        root = TreeNode(num)
                        root.left = l
                        root.right = r
                        res.append(root)
            return res
        if n==0: return []
        trees = getNodes([i+1 for i in range(n)])
        return trees