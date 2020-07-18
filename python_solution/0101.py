# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # Solution 1: Recursive
        if not root: return True
        def Mirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and Mirror(left.left, right.right) and Mirror(left.right, right.left)
        return Mirror(root.left, root.right)
        
        # Solution 2: Iterative
        if not root: return True
        ele = [root.left, root.right]
        while ele:
            p, q = ele[0], ele[1]
            ele = ele[2:]
            if not p and not q:
                continue
            if not p or not q: return False
            if p.val != q.val: return False
            ele.append(p.left)
            ele.append(q.right)
            ele.append(p.right)
            ele.append(q.left)
        return True