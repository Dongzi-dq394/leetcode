# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        odd, even = head, head.next
        temp = even
        while temp and temp.next:
            odd.next = temp.next
            temp.next = temp.next.next
            odd = odd.next
            temp = temp.next
        odd.next = even
        return head