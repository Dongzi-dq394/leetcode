# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # Old Solution: Divide and Conquer Using TwoLists (148ms: 50%)
        if not lists: return None
        if len(lists)==1: return lists[0]
        middle = len(lists)//2
        left = self.mergeKLists(lists[:middle])
        right = self.mergeKLists(lists[middle:])
        def mergeTwoLists(l1, l2):
            if not l1 or not l2: return l1 or l2
            if l1.val < l2.val:
                l1.next = mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = mergeTwoLists(l1, l2.next)
                return l2
        return mergeTwoLists(left, right)
        
        # New Solution: Priority Queue from Solution (184ms)
        # We can also use heap to do this (totally same)
        from queue import PriorityQueue
        head = temp = ListNode()
        q = PriorityQueue()
        for i, l in enumerate(lists):
            if l:
                # we can't use priority queue to compare the listnode
                #q.put((l.val, l))
                q.put((l.val, i))
        while not q.empty():
            (val, index) = q.get()
            temp.next = ListNode(val)
            temp = temp.next
            lists[index] = lists[index].next
            if lists[index]:
                q.put((lists[index].val, index))
        return head.next