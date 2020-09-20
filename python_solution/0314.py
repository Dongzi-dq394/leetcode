# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        dic = defaultdict(list)
        stack = [(root, 0)]
        while stack:
            length = len(stack)
            for i in range(length):
                node, index = stack.pop(0)
                dic[index].append(node.val)
                if node.left:
                    stack.append((node.left, index-1))
                if node.right:
                    stack.append((node.right, index+1))
        key = list(dic.keys())
        key.sort()
        res = []
        for item in key:
            res.append(dic[item])
        return res