# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        string=""
        curr=head
        if curr==None:
            return False
        #traversing the linked list
        while(curr!=None):
            string+=str(curr.val)
            curr=curr.next
        
        revstring="".join(reversed(string))
        if revstring==string:
            return True
        return False


        