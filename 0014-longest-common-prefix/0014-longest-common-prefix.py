class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #prefix vaneko agadi ko chai ho 
        #not like common substring
        strs.sort()
        print(strs)
        # common string
        string=""
        # after sorting ,if they have common prefix, we can just compare between first and last,
        l=0
        r=0
        n=min(len(strs[0]),len(strs[-1]))
        while(l<n and r<n):
            if strs[0][l]==strs[-1][r]:
                
                string+=strs[0][l]
                l+=1
                r+=1
            else:
                break
        return string

       


        