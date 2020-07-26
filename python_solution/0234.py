# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        res = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            temp = slow
            slow = slow.next
            temp.next = res
            res = temp
        if fast:
            slow = slow.next
        while res and res.val == slow.val:
            res = res.next
            slow = slow.next
        return not res