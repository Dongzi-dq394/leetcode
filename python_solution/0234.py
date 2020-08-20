# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Solution 1: Reverse the whole list using extra space (108ms: 23.60%)
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr==arr[::-1]
        
        # Solution 2: Reverse the first half list in-place (68ms: 90.66%)
        # less space than the first one
        if not head: return True
        slow = fast = head
        rev = ListNode()
        while fast and fast.next:
            fast = fast.next.next
            temp = slow
            slow = slow.next
            temp.next = rev.next
            rev.next = temp
        if fast:
            slow = slow.next
        rev = rev.next
        while slow:
            if rev.val!=slow.val:
                return False
            rev = rev.next
            slow = slow.next
        return True