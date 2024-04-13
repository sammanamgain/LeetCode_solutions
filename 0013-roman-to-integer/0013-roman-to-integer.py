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
                print(combined)
                
                ans+=int(dictionary[str(combined)])
                print("answer",ans)
                print(dictionary[str(combined)])
              
                i+=2
                print(i)
            elif s[i] in dictionary:
                print(s[i])
                print(dictionary[s[i]])
                ans+=int(dictionary[s[i]])
                print("answer",ans)
                i+=1
                print(i)
        return ans
        