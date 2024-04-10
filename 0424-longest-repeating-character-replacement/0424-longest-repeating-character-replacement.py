class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        Max=0
        left=0
        right=0
        hashmap={}
   
        while(right<len(s)):
         
            #adding each element in hashmap
            if s[right] in hashmap:
                hashmap[s[right]]+=1
            else:
                hashmap[s[right]]=1
            #length of windows
            length=right-left+1
            #find maximum element of hashmap
            frequent=0
            for key,value in hashmap.items():
                frequent=max(frequent,value)
            # find subtraction of window length and frequent number 
            # this help to replace character, if length is 5, ferquent is 3, we can replace k (2),
            #which makes valid window
            remaining=length-frequent
            if remaining<=k:
                Max=max(Max,length)
            else:
                hashmap[s[left]]=hashmap[s[left]]-1
                left+=1
            right+=1


            

        return Max

                
        