class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        ans=0
        if (len(nums)%2!=0):
            nums.append(0)
        for i in range(1,len(nums),2):
            #print(i)
            if nums[i]!=nums[i-1]:
                ans=nums[i-1]
                break
        return ans
    
            