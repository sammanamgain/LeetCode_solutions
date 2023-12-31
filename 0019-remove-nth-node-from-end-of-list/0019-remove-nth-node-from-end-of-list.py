# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        order=1
        while(curr.next!=None):
            curr=curr.next
            order=order+1
        toindex=(order-n-1)
        single=None
        if(toindex==-1):
            toindex=0
            single=0
        
        index=0
        curr=head
        while(curr!=None):
            if(index==toindex):
                if(single==0):
                    head=curr.next
                    return head
                print(curr.val)
                i=0
                copy=curr
                while(i!=2 ) :
                    if(copy.next==None):
                        copy=None
                        break
                    copy=copy.next
                    i=i+1
                    
                curr.next=copy
                return head
            curr=curr.next
            index=index+1
        return head
                
                
        
        