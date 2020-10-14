# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        # Solution by myself: Recursion (36ms: 64.65%)
        res = 0
        def helper(node):
            nonlocal res
            if not node: return None
            left, right = helper(node.left), helper(node.right)
            if left==None and right==None:
                res += 1
                return node.val
            if left==None and right!=None:
                if node.val==right:
                    res += 1
                    return node.val
                return '*'
            if left!=None and right==None:
                if node.val==left:
                    res += 1
                    return node.val
                return '*'
            if node.val==left and node.val==right:
                res += 1
                return node.val
            return '*'
        helper(root)
        return res