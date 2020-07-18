# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        stack = [root]
        level = 1
        while stack:
            length = len(stack)
            temp = []
            for i in range(length):
                node = stack.pop(0)
                temp.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            if level%2==0:
                res.append(temp[::-1])
            else:
                res.append(temp)
            level += 1
        return res