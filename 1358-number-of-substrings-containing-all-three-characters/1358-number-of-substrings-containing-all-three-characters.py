class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        #bruteforce
    
        # totalstring=0
        # left=0
        # right=0
        # hashmap={}
        # string=""
     
        # while(left<len(s)):
           
           
        #     string+=s[right]
            
        #     if s[right] not in hashmap:
        #         hashmap[s[right]]=1
               
        #     if len(hashmap)>=3:
        #         totalstring+=1
        #         extra=len(s)-right-1
        #         totalstring+=extra
        #         left+=1
        #         right=left
        #         hashmap.clear()
        #         string=""
                
        #     else:   
        #         right+=1
        #         if right>len(s)-1:
        #             break
        # return totalstring
        #to check if a, b, c exists or not
        abc=[-1,-1,-1]
        count=0
        for i in range(len(s)):
            if s[i]=='a':
                abc[0]=i
            elif s[i]=='b':
                abc[1]=i
            elif s[i]=='c':
                abc[2]=i
           
            if abc[0]!=-1 and abc[1]!=-1 and abc[2]!=-1:
                count+=1
                Min=min(abc)
                count+=Min
                

        return count
            


            
                
            
        