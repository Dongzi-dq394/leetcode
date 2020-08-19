# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # New Solution 1: Iteratively (60ms: 17.42%)
        res = ListNode()
        while head:
            new = ListNode(head.val)
            new.next = res.next
            res.next = new
            head = head.next
        return res.next
        
        # New Solution 2: Recursively (40ms: 58.31%)
        def helper(node):
            if not node.next:
                return node, node
            head, tail = helper(node.next)
            node.next = None
            tail.next = node
            return head, node
        if not head: return head
        res, tail = helper(head)
        return res
        
        # New Solution 3: from discussion (28ms: 97.57%)
        if not head or not head.next: return head
        res = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return res