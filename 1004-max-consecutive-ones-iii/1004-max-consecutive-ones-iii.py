class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #find the longest subarray with at least k zeros
        left=0
        right=0
        zerocount=0
        Max=0
        
        while(right<len(nums) and left<len(nums)):
            if nums[right]==0:
                zerocount+=1
            
            if zerocount>k:
                if nums[left]==0:
                    zerocount-=1
                    
                left+=1
                right+=1
                            
            else:
                Max=max(Max,right-left+1)
                right+=1
        
        return Max

           



           



        