class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # we are going to  use DNF algorithm
        low=0
        mid=0
        high=len(nums)
        while(mid<high):
            if(nums[mid]==0):
                temp=nums[mid]
                nums[mid]=nums[low]
                nums[low]=temp
                low+=1
                mid+=1
            elif(nums[mid]==1):
                mid+=1
            else:
                temp=nums[high-1]
                nums[high-1]=nums[mid]
                nums[mid]=temp
                high-=1
