# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        demo = None

        while curr != None:
            x = curr.next
            curr.next = demo
            if x == None:
                head = curr
                return head

            demo1 = x.next if (x) else None

            demo = x

            x.next = curr
            if demo1 == None:
                head = x
                return head
            curr = demo1

        return head
