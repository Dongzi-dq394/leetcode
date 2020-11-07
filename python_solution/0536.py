# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        # Solution 1: Stack + DFS (92ms: 94.79%)
        if not s: return None
        ele = s.split('(')
        head = TreeNode()
        stack = [head]
        temp = 0
        right = False
        for item in ele:
            if item[-1]!=')':
                number = int(item)
                nextright = False
                nexttemp = 0
            else:
                nextright = True
                nexttemp = 0
                for i in range(len(item)-1, -1, -1):
                    if item[i]==')':
                        nexttemp += 1
                    else:
                        break
                number = int(item[:-nexttemp])
            newnode = TreeNode(number)
            for _ in range(temp):
                stack.pop()
            temp = nexttemp
            if right:
                stack[-1].right = newnode
                stack.append(newnode)
            else:
                stack[-1].left = newnode
                stack.append(newnode)
            right = nextright
        return head.left
        
        # Solution 2 from Discussion: Tricky Stack (88ms: 97.92%)
        if not s: return None
        string = ''
        stack = []
        for char in s:
            if char not in '()':
                string += char
            else:
                if string:
                    node = TreeNode(int(string))
                    string = ''
                    stack.append(node)
                if char==')':
                    child = stack.pop()
                    if stack[-1].left:
                        stack[-1].right = child
                    else:
                        stack[-1].left = child
        return stack[0] if stack else TreeNode(int(s))