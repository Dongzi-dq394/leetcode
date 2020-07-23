# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Something to learn from this problem:
        # 1. Recursive way need much more memory than the iterative method
        
        # Solution 1: Recursive method (By myself: 1620ms)
        if not head or not head.next: return head
        temp = head
        while temp.next and temp.next.next:
            temp = temp.next
        res = temp.next
        temp.next = None
        res.next = self.reverseList(head)
        return res
        
        # Solution 2: Iterative method (40ms)
        res = None
        while head:
            node = ListNode(head.val)
            node.next = res
            res = node
            head = head.next
        return res
        
        # Solution 3: Recursive method (from solutions: 32ms)
        if not head or not head.next: return head
        res = self.reverseList(head.next)
        # head.next is the last ele in res, and then we should add head to it
        head.next.next = head
        # head should be the final ele in res, so we should set its next None
        head.next = None
        return res