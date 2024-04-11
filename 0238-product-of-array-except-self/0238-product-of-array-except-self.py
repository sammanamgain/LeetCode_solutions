class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # in this approach, we calculate prefix and postfix
        
        n=len(nums)-1
        output=[0]*(n+1)
        product=1
        #calculating prefix
        for i in range(n+1):
            if i==0:
               
                output[i]=1
            else:
                
                product*=nums[i-1]
                output[i]=product
       
        #calculating postfix and directly accumulating result
        postfix=1
        for i in range(n,-1,-1):
            output[i]=output[i]*postfix
            postfix=postfix*nums[i]
        return output
                

        
                
            
            
        