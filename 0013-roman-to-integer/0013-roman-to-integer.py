class Solution:
    def romanToInt(self, s: str) -> int:
        ans=0
        i=0
        dictionary={'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900,'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        while(i<len(s)):
            combined=""
            if i<=len(s)-2:
                combined=s[i]+s[i+1]
         
            if combined in dictionary:
                
                
                ans+=int(dictionary[str(combined)])
               
              
                i+=2
               
            elif s[i] in dictionary:
               
                ans+=int(dictionary[s[i]])
               
                i+=1
              
        return ans
        