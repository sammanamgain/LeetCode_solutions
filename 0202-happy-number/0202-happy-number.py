class Solution:
    def isHappy(self, n: int) -> bool:
        result=set()
        result.add(0)

        if n==1 :
            return True
        
        else:
            sum=0
         
            while(sum==0):
                while(n>=1):
                    sum+=(n%10)*(n%10)
                    n=n//10
                
           
                if sum==1:
                    return True
                # print(sum,original)
                elif  sum in result:
                    return False
                
                else:
                    n=sum
                    print(n)
                    result.add(n)
                    sum=0
                    
            
                
            

        
            


        