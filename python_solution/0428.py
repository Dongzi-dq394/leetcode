"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        def helper(node):
            if not node: return ''
            if not node.children: return str(node.val)
            res = str(node.val)+'['
            for i in range(len(node.children)-1):
                res += helper(node.children[i])
                res += ' '
            res += helper(node.children[-1])
            res += ']'
            return res
        string = helper(root)
        #print(string)
        return string
        
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data: return None
        start = 0
        while start<len(data) and data[start]!='[':
            start += 1
        root = Node(int(data[:start]), [])
        new_str = []
        count = 0
        left = start+1
        for i, char in enumerate(data[start+1:-1]):
            if char=='[':
                count += 1
            elif char==']':
                count -= 1
            elif char==' ':
                if count==0:
                    new_str.append(data[left:i+start+1])
                    left = i+2+start
        if data[left:-1]!='':
            new_str.append(data[left:-1])
        for sub_str in new_str:
            root.children.append(self.deserialize(sub_str))
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))