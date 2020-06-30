# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        length = len(lists)
        if length == 1: return lists[0]
        else:
            middle = length // 2
            temp_l1 = self.mergeKLists(lists[:middle])
            temp_l2 = self.mergeKLists(lists[middle:])
            return self.mergeTwoLists(temp_l1, temp_l2)