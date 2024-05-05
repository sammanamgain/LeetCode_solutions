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
        # we donot have access to previous node, which is pointing to given node,
        # we are going to copy all value from next node to current node,
        # so that means current node value and next is overwritten by next node, which is also deletion
        # but we delete next node , which means next node value is copied in current node, so previous next node is ultimately deleted

        node.val,node.next=node.next.val,node.next.next
        