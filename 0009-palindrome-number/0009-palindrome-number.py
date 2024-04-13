class Solution:
    def isPalindrome(self, x: int) -> bool:
        sx=str(x)
        x=list(sx)
   
        y="".join(reversed(x))
        if sx==y:
            return True
        else:
            return False

        