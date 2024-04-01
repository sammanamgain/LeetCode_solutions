class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sum=n*(n+1)//2
        forsum=0
        for i in nums:
            forsum+=i
        #checking if zero exists or not
        if 0 not in nums:
            return 0
        if(forsum!=sum):
            return sum-forsum
            
        
        