# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    # Solution 1: preorder + recursion from discussion (152ms: 61%)
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return '[]'
        res = []
        def preorder(node):
            if node:
                res.append(node.val)
                preorder(node.left)
                preorder(node.right)
            else:
                res.append(None)
        preorder(root)
        return str(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.lstrip('[').rstrip(']')
        if not data: return None
        data = data.split(', ')
        def build():
            val = data.pop(0)
            if val =='None':
                return None
            root = TreeNode(int(val))
            root.left = build()
            root.right = build()
            return root
        return build()
    

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))