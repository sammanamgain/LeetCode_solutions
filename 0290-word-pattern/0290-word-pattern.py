class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        characterlist=s.split(' ')
        hashmap={}
        hashmap1={}
        if len(characterlist)!=len(pattern):
            return False
        for i,j in zip(pattern,characterlist):
            if i not in hashmap:
                hashmap[i]=j

            else:
                if hashmap[i]!=j:
                    return False
            if j not in hashmap1:
                hashmap1[j]=i

            else:
                
                if hashmap1[j]!=i:
                    return False


        return True
        