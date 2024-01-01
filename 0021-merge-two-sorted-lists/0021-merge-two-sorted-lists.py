# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged=ListNode()
        curr=merged
        firstlist=[]
        secondlist=[]
        while(list1):
            firstlist.append(list1.val)

            list1=list1.next

        while(list2):
            secondlist.append(list2.val)
            list2=list2.next
        combined=firstlist+secondlist

        combined.sort()
     
        for item in combined:
            intermediate=ListNode()
            intermediate.val=item
           
            curr.next=intermediate
            curr=curr.next
        return merged.next

        