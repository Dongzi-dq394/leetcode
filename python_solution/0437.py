# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # Solution 1: Recursion + BFS (972ms: 22.47%)
        def helper(node, target):
            res = 0
            if node.val == target:
                res += 1
            if node.left:
                res += helper(node.left, target-node.val)
            if node.right:
                res += helper(node.right, target-node.val)
            return res
        if not root: return 0
        res = 0
        stack = [root]
        while stack:
            length = len(stack)
            for i in range(length):
                node = stack.pop(0)
                res += helper(node, sum)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return res
        
        # Solution 2: Memo and DFS from discussion (88ms: 65%)
        dic = defaultdict(int)
        dic[0] = 1
        res = 0
        def helper(node, cur, target):
            nonlocal res
            if not node: return
            cur += node.val
            old = cur-target
            res += dic[old]
            dic[cur] += 1
            helper(node.left, cur, target)
            helper(node.right, cur, target)
            # Important!!!
            # After calling node.left and node.right, the branch of cur has been used.
            dic[cur] -= 1
        helper(root, 0, sum)
        return res