class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # logically breaking array into two part from 0 to k and k to end of list
        # reversing both of them individually
        # reversing whole array then
        # here we arenot dividing phycially ,so no extra space is required
        #for k>length of nums,we can reduce to upto lenth,using modules as result is same
        k=k % len(nums)
        i=len(nums)-k
        
        nums[0:i]=reversed(nums[0:i])
        nums[i:len(nums)]=reversed(nums[i:len(nums)])
        nums.reverse()