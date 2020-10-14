# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        # Solution myself+Solution: Tree + Recursion (48ms: 60.35%)
        if not root: return []
        left = []
        temp = root.left
        while True:
            if temp:
                left.append(temp.val)
            else:
                break
            if temp.left:
                temp = temp.left
            elif temp.right:
                temp = temp.right
            else:
                break
        right = []
        temp = root.right
        while True:
            if temp:
                right.append(temp.val)
            else:
                break
            if temp.right:
                temp = temp.right
            elif temp.left:
                temp = temp.left
            else:
                break
        leaves = []
        def helper(node):
            if not node: return
            if not node.left and not node.right:
                leaves.append(node.val)
                return
            helper(node.left)
            helper(node.right)
        helper(root)
        if not left and not right:
            return leaves
        return [root.val]+left[:-1]+leaves+right[::-1][1:]