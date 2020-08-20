# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # Old Solution: In-order traverse (64ms: 41.39%)
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                break
            root = stack.pop()
            k -= 1
            if k==0:
                return root.val
            root = root.right
        
        # New Solution: Memoization --> from ALGO course (52ms: 81.00%)
        self.memo = {}
        def helper(node):
            if not node: return 0
            if node in self.memo: return self.memo[node]
            left = helper(node.left)
            right = helper(node.right)
            self.memo[node] = left+right+1
            return left+right+1
        def check(node, k):
            left_num = self.memo[node.left] if node.left else 0
            if left_num == k-1:
                return node.val
            elif left_num >= k:
                return check(node.left, k)
            else:
                return check(node.right, k-left_num-1)
        helper(root)
        return check(root, k)