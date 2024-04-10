class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
    
        # this approch calculate no of subarray which sum is <=goal
        def subarray(goal):
            if goal<0:
                return 0
            count=0
            l,r=0,0
            sum=0
            while(r<len(nums)):
                sum+=nums[r]

                
                while(sum>goal):
                    sum-=nums[l]
                    l+=1
                if sum<=goal:
                    count+=(r-l+1)
                    r+=1
            print(count)
            return count
            
        return subarray(goal)-subarray(goal-1)

                
                

     
   
        


  