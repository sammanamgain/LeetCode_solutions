class Solution:
    def reverseWords(self, s: str) -> str:
        s=" "+s+" "
        ans=""
        firstindex=-1
        for i in range(len(s)-2,-1,-1):
            if s[i] !="" and s[i]!=" " and s[i+1]==" ":
                firstindex=i
                print(firstindex)
            elif s[i]==" " or s[i]=="":
                if s[i+1]!=" " and  s[i+1]!="":
                    ans=ans+s[i+1:firstindex+1]+" "
                    print(ans)
        n=len(ans)
        
        return ans[0:n-1]


        

        