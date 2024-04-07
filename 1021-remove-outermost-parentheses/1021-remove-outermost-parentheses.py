class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        ans=""
        inital=0
        for i in range(len(s)):
            if len(stack)==0:
                inital=i
            if s[i]=="(":
                stack.append(s[i])
            elif s[i]==')':
                stack.pop()
            if len(stack)==0:
                final=i
                ans=ans+s[inital+1:final]
        return ans      




        