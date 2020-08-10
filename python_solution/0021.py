# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Solution 1: Link List
        if not l1 and not l2: return None
        head = ListNode()
        res = head
        while l1 and l2:
            if l1.val <= l2.val:
                head.val = l1.val
                l1 = l1.next
            else:
                head.val = l2.val
                l2 = l2.next
            head.next = ListNode()
            head = head.next
        if l1:
            head.val = l1.val
            head.next = l1.next
        if l2:
            head.val = l2.val
            head.next = l2.next
        return res
        
        # Solution 2: Recursive
        if not l1: return l2
        if not l2: return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

        # New Solution: Recursion (40ms: 70%)
        if not l1 or not l2: return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2