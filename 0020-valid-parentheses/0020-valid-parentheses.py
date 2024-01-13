class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i=='(' or i=='{' or i=='[' :
              stack.append(i)
            if i==')' or i=='}' or i==']':
                if stack:
                  current=stack[-1]
                else:
                    return False
                if current=='(':
                    if i==')':
                        stack.pop()
                    else:
                        return False
                elif current=='{':
                    if i=='}':
                        stack.pop()
                    else:
                        return False
                else:
                    if i==']':
                        stack.pop()
                    else:
                        return False
        if not stack:
          return True
        else:
          return False
