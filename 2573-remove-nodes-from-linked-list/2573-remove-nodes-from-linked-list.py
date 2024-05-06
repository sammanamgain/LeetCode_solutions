# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recursive solution:

        if head==None:
            return
        # left side of head.next inclues only node greater than current head
        head.next=self.removeNodes(head.next)

        if head.next and head.val<head.next.val:
            # deleting current node
            return head.next
        return head
        

