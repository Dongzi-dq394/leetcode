# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder and not inorder: return None
        index = inorder.index(preorder[0])
        res = TreeNode(preorder[0])
        res.left = self.buildTree(preorder[1:index+1], inorder[:index])
        res.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return res