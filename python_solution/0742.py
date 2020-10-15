# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        # Solution from Solution: Graph + BFS (48ms: 76.16%)
        edges = defaultdict(list)
        def helper(node, pre):
            if node:
                edges[pre].append(node)
                edges[node].append(pre)
                helper(node.left, node)
                helper(node.right, node)
        helper(root, None)
        queue = deque([node for node in edges if node and node.val==k])
        visited = set(queue)
        while queue:
            node = queue.popleft()
            if node:
                if len(edges[node])<=1:
                    return node.val
                for v in edges[node]:
                    if v not in visited:
                        visited.add(v)
                        queue.append(v)