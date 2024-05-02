class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        # coll=set(nums)
        # print(nums)
        # while(1):
        #     if len(nums)==0:
        #         return -1
        #     currmax=max(nums)
        #     if (-currmax) in coll:
        #         return currmax
        #     else:
        #         nums.remove(currmax)
        #         print(nums)
        
        nums.sort()
        l=0
        r=len(nums)-1
        while(l<r):
            if nums[l]==(-(nums[r])):
                return nums[r]
            else:
                if (-(nums[l])>nums[r]):
                    l+=1
                else:
                    r-=1
        
        return -1