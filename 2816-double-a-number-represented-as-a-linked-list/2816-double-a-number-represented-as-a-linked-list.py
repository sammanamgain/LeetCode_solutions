# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def multiply_and_returnCarry(node:ListNode):
            if node==None:
                return 0
            val=(node.val*2) + multiply_and_returnCarry(node.next)
       
            node.val=val%10
            
            return val//10
        
        final_Carry=multiply_and_returnCarry(head)
        if final_Carry:
            newnode=ListNode(final_Carry)
            curr=head
            head=newnode
            newnode.next=curr
        return head



        

            

            
        