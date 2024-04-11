class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap={}
        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]]='repeated'
            else:
                hashmap[s[i]]=i
            
        firstindex=-1
        for key,value in hashmap.items():
            if value!='repeated':
                firstindex=value
                break
        return firstindex


        
        