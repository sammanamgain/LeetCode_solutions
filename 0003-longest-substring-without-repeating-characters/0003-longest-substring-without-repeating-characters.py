class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       #sliding window problem
        i=0 #right
        j=0  #left
        Max=0
        charset=set()
        for i in range(len(s)):
            while s[i] in charset:
                charset.remove(s[j])
                j=j+1
            
            charset.add(s[i])
            Max=max(Max,i-j+1)
            
         
        return Max
            