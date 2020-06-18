# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        add = int((l1.val + l2.val) / 10)
        result = ListNode(val = (l1.val+l2.val)%10)
        head = result
        l1, l2 = l1.next, l2.next
        while l1 and l2:
            result.next = ListNode()
            result = result.next
            temp = l1.val + l2.val + add
            add = int(temp / 10)
            result.val = temp % 10
            l1 = l1.next
            l2 = l2.next
        while l1:
            result.next = ListNode()
            result = result.next
            temp = l1.val + add
            add = int(temp / 10)
            result.val = temp % 10
            l1 = l1.next
        while l2:
            result.next = ListNode()
            result = result.next
            temp = l2.val + add
            add = int(temp / 10)
            result.val = temp % 10
            l2 = l2.next
        if add == 1:
            result.next = ListNode(val = 1)
        return head