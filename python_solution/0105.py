# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # Solution 1 by myself: Recursion (212ms: 37.47%) --> waste space
        if not preorder: return None
        index = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:1+index], inorder[:index])
        root.right = self.buildTree(preorder[1+index:], inorder[index+1:])
        return root
        
        # New Solution from discussion: Use Pre-order and In-order (84ms: 72.24%)
        # Very smart!!
        def helper(last):
            if preorder and inorder[-1]!=last:
                root = TreeNode(preorder.pop())
                root.left = helper(root.val)
                inorder.pop()
                root.right = helper(last)
                return root
        preorder.reverse()
        inorder.reverse()
        return helper(None)