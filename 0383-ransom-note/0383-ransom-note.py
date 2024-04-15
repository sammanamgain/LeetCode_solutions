class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap={}
        for i in magazine:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        
        for i in ransomNote:
            if i in hashmap:
                hashmap[i]-=1
                if hashmap[i]==0:
                    hashmap.pop(i)
            else:
                return False
        return True
            
            
        