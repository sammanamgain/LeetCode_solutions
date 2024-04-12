class Solution(object):
    def lengthOfLongestSubstring(self, s):
        hashmap={}
        l=0
        r=0
        count=0
        while(r<len(s)):
            if s[r] not in hashmap:
                count=max(count,r-l+1)
                hashmap[s[r]]=1
                print(s[r])
                r+=1
                
                
                print(hashmap)
            else:
                print(hashmap)
                hashmap[s[l]]= hashmap[s[l]]-1
                if hashmap[s[l]]==0:
                    hashmap.pop(s[l])
                l+=1
            
        return count







        