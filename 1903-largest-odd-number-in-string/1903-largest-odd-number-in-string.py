class Solution:
    def largestOddNumber(self, num: str) -> str:
        right=len(num)-1
        while(right>=0):
            if int(num[right])%2!=0:
                return num[0:right+1]
            right-=1
        
        return ""

        