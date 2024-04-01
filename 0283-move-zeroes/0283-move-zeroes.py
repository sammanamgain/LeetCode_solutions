class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # finding the position of first o
        j=-1
        for i in range(len(nums)):
            if nums[i]==0:
                j=i
                break
        # using two pointer approach, set i =j+1, which check if there is non zero element , if found,swap it
        # j alaways points to zero
        if j!=-1:
            
            for i in range(j+1,len(nums)):
                if nums[i]!=0:
                    nums[j]=nums[i]
                    nums[i]=0
                    j=j+1
            
        
        
            