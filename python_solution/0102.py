# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        stack = [root]
        while stack:
            length = len(stack)
            temp = []
            for i in range(length):
                temp.append(stack[i].val)
                if stack[i].left:
                    stack.append(stack[i].left)
                if stack[i].right:
                    stack.append(stack[i].right)
            res.append(temp)
            stack = stack[length:]
        return res