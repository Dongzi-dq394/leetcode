# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        p1 = head
        p2 = slow.next
        slow.next = None
        
        res1 = self.sortList(p1)
        res2 = self.sortList(p2)
        return self.mergeSort(res1, res2)
    
    def mergeSort(self, n1, n2):
        res = ListNode()
        temp = res
        while n1 and n2:
            if n1.val < n2.val:
                temp.next, n1 = n1, n1.next
            else:
                temp.next, n2 = n2, n2.next
            temp = temp.next
        if n1:
            temp.next = n1
        if n2:
            temp.next = n2
        return res.next
                