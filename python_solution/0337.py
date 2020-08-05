# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        # TLE at the last test case
        # Naive recursion
        '''
        def helper(node):
            if not node: return 0
            value = 0
            if node.left:
                value += helper(node.left.left)+helper(node.left.right)
            if node.right:
                value += helper(node.right.left)+helper(node.right.right)
            return max(node.val+value, helper(node.left)+helper(node.right))
        return helper(root)
        '''
        # Solution 1: improvement from the previous one using DP
        # to avoid many repeating sub-problems (56ms: 59.43%)
        dic = {}
        def helper(node):
            if not node: return 0
            if node in dic: return dic[node]
            value = 0
            if node.left:
                value += helper(node.left.left)+helper(node.left.right)
            if node.right:
                value += helper(node.right.left)+helper(node.right.right)
            res = max(node.val+value, helper(node.left)+helper(node.right))
            dic[node] = res
            return res
        return helper(root)
        
        # Solution 2: Recursion but with more specific result
        # helper(node) returns [node_use, node_not] (124ms: 6.05%)
        def helper(node):
            if not node: return (0,0)
            left = helper(node.left)
            right = helper(node.right)
            return (node.val+left[1]+right[1], max(left)+max(right))
        return max(helper(root))