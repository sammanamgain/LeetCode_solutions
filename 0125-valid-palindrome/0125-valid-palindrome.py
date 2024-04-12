class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s==" ":
            return True
       
        s=s.lower()
        # using list comprehension
        arr=[i for i in s if i.isalnum()]
        s="".join(arr)

        reversedstring=reversed(s)
        reversedstring="".join(reversedstring)
        
        if reversedstring==s:
            return True
        return False

        
        