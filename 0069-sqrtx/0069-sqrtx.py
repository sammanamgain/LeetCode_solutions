class Solution:
    def mySqrt(self, x: int) -> int:
        exceeded_value=0
        if x==1 or x==2 or x==3:
            return 1
        if x==0:
            return 0
       
        for i in range(1,(x//2)+1):
            if (i*i)==x:
                return i
            elif (i*i)>x:
                exceeded_value=i
                break
       
        return (exceeded_value-1)
        