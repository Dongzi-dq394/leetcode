# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        ele = []
        def inorder(root):
            if root.left:
                inorder(root.left)
            ele.append(root.val)
            if root.right:
                inorder(root.right)
        inorder(root)
        for i in range(len(ele)-1):
            if ele[i] >= ele[i+1]:
                return False
        return True