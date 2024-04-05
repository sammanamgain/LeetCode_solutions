class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap={}
        left=0
        right=0
        Max=0
        while(right<len(s)):
            if (s[right] in hashmap):
                if left<=hashmap[s[right]]:
                    left=hashmap[s[right]]+1
                hashmap[s[right]]=right
                
            else:
                
                hashmap[s[right]]=right
            Max=max(Max,right-left+1)
            
            right+=1

  
        return Max
        