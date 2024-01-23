class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # just using the for loops
        length=len(s)
        for i in range(0,length//2):
            temp =s[length-i-1]
            s[length-i-1]=s[i]
            s[i]=temp
            
            
            
            
        