# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB: return None
        
        l1 = l2 = 0
        temp1, temp2 = headA, headB
        while temp1:
            l1 += 1
            temp1 = temp1.next
        while temp2:
            l2 += 1
            temp2 = temp2.next
        diff = abs(l1-l2)
        
        temp1, temp2 = headA, headB
        if l1 >= l2:
            while diff:
                temp1 = temp1.next
                diff -= 1
            while temp1 != temp2:
                temp1 = temp1.next
                temp2 = temp2.next
            return temp1
        else:
            while diff:
                temp2 = temp2.next
                diff -= 1
            while temp1 != temp2:
                temp1 = temp1.next
                temp2 = temp2.next
            return temp1