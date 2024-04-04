class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        Max= float('-inf')
        sum=0
        startindex=0
        finalindex=0

        for i in nums:
            if sum==0:
                startindex=i
            sum+=i
            if (sum>Max):
                Max=sum
                finalindex=i
            if(sum<0):
                sum=0
        return Max

                
                

            
        