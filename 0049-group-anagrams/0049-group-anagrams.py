class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for i in strs:
            
            k=sorted(i)
            key=""
            key=key.join(k)

   
            if key in hashmap:
                hashmap[key].append(i)
            else:
                hashmap[key]=[i]
        
        output=[]
        for key,value in hashmap.items():
            output.append(value)
        return output