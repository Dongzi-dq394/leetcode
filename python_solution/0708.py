"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        # Solution from Solution: Two Pointers (40ms: 48.35%)
        if not head:
            res = Node(insertVal)
            res.next = res
            return res
        flag = False
        cur, nex = head, head.next
        while True:
            if cur.val<=insertVal<=nex.val:
                flag = True
            elif cur.val>nex.val:
                if insertVal>=cur.val or insertVal<=nex.val:
                    flag = True
            if flag:
                cur.next = Node(insertVal, nex)
                return head
            cur = cur.next
            nex = nex.next
            if cur==head:
                break
        cur.next = Node(insertVal, nex)
        return head