# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # node = node.next
        # This line is wrong because node is like a pointer, if we want to
        # modify the value, we need to modify the value which pointer pointing
        # at. Or, we only move the pointer to the next node.
        node.val, node.next = node.next.val, node.next.next