"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Codec:
    # Solution from Solution: BFS with some tricks (84ms: 37.84%)
    
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        if not root: return None
        res = TreeNode(root.val)
        queue = deque([(res, root)])
        while queue:
            parent, cur = queue.popleft()
            temp = TreeNode(0)
            head = temp
            for child in cur.children:
                newNode = TreeNode(child.val)
                temp.right = newNode
                queue.append((newNode, child))
                temp = temp.right
            parent.left = head.right
        return res
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        if not data: return None
        res = Node(data.val, [])
        queue = deque([(res, data)])
        while queue:
            parent, cur = queue.popleft()
            start = cur.left
            while start:
                child = Node(start.val, [])
                parent.children.append(child)
                queue.append((child, start))
                start = start.right
        return res
                

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))