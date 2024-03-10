class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramslist={}
        result=[]
        
        for s in strs:
            sorteds=tuple(sorted(s))
            if sorteds in anagramslist:
                anagramslist[sorteds].append(s)
            else:
                anagramslist[sorteds]=[]
                anagramslist[sorteds].append(s)
        
        for i in anagramslist.values():
            result.append(i)
        return result
                
        