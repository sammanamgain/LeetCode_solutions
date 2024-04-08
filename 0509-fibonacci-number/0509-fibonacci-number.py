class Solution:
    def fib(self, n: int) -> int:
        a=0
        b=1
        c=0
        if n==1:
            return 1
        if n==0:
            return 0
        for i in range(2,n+1,1):
            c=a+b
            temp=b
            b=c
            a=temp

        return c
        