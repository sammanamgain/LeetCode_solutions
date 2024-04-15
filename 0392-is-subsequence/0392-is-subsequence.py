class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # using two pointer approach
        l=0
        r=0
        while(l<len(s) and r<len(t)):
            left=s[l]
            right=t[r]
            if s[l]==t[r]:
                l+=1
                r+=1
            else:
                r+=1
            
        if l<len(s):
            return False


        return True
