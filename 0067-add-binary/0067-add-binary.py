class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result=""
        carry=0
        ML=max(len(b),len(a))

        #making same length
        if ML>len(b):
            diff=ML-len(b)
            for i in range(diff):
                b="0"+b
            
        elif ML>len(a):
            diff=ML-len(a)
            for i in range(diff):
                a="0"+a
         
        # working on operation (adding)
  
        for i in range(ML-1,-1,-1):
            r=int(a[i])+int(b[i])+carry
            carry=0
        
            if r==2:
                carry=1
                r=0
            if r==3:
                carry=1
                r=1
           
            result=str(r)+result
         
        if carry==1:
            result=str(carry)+result
        

        return result

        