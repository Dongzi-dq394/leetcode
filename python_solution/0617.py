# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # Solution 1: recursion (80ms: 99.54%)
        if not t1 or not t2: return t1 or t2
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
        
        # Solution 2 from discussion: iterative (100ms: 57.75%)
        if not t1 or not t2: return t1 or t2
        stack = [[t1, t2]]
        while stack:
            temp = stack.pop()
            # This line is important!!
            if not temp[0] or not temp[1]:
                continue
            temp[0].val += temp[1].val
            if not temp[0].left:
                temp[0].left = temp[1].left
            else:
                stack.append([temp[0].left, temp[1].left])
            if not temp[0].right:
                temp[0].right = temp[1].right
            else:
                stack.append([temp[0].right, temp[1].right])
        return t1