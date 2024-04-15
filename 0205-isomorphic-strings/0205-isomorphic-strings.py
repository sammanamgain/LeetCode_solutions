class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        hashmap1={}
        l = 0
        r = 0
        if len(s)!=len(t):
            return False
        while l < len(s) and r < len(t):
            if s[l] not in hashmap:

                hashmap[s[l]] = t[r]
              
            else:
                if hashmap[s[l]] == t[r]:
                    pass
                   
                else:
                    return False
            if t[r] not in hashmap1:

                hashmap1[t[r]] = s[l]
                l += 1
                r += 1
            else:
                if hashmap1[t[r]] == s[l]:
                    l += 1
                    r += 1
                else:
                    return False
        return True
            
