# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        # Solution by hint: Inorder traversal in each node (180ms: 6.80%)
        ans = 0
        def helper(node):
            res = []
            stack = []
            while True:
                while node:
                    stack.append(node)
                    node = node.left
                if not stack:
                    break
                node = stack.pop()
                if res and res[-1]>=node.val:
                    return -1
                res.append(node.val)
                node = node.right
            return len(res)
        def checker(node):
            if not node: return 0
            nonlocal ans
            ans = max(ans, helper(node))
            checker(node.left)
            checker(node.right)
        checker(root)
        return ans
        
        # Solution from Discussion: Recursion with trick (52ms: 60.06%)
        def helper(node):
            if not node:
                return 0, 0, float('Inf'), -float('Inf')
            l1, l2, l3, l4 = helper(node.left)
            r1, r2, r3, r4 = helper(node.right)
            if l4<node.val<r3:
                temp = l2+r2+1
            else:
                temp = -float('Inf')
            return max(l1, r1, temp), temp, min(node.val, l3, r3), max(node.val, l4, r4)
        return helper(root)[0]