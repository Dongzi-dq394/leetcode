"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # Hash Table is the key!!!
        if not head: return None
        temp = head
        dic = {}
        while temp:
            node = Node(temp.val)
            dic[temp] = node
            temp = temp.next
        temp = head
        while temp:
            if temp.next:
                dic[temp].next = dic[temp.next]
            if temp.random:
                dic[temp].random = dic[temp.random]
            temp = temp.next
        return dic[head]