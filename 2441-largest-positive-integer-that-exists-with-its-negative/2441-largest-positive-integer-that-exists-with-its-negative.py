class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        coll=set(nums)
        print(nums)
        while(1):
            if len(nums)==0:
                return -1
            currmax=max(nums)
            if (-currmax) in coll:
                return currmax
            else:
                nums.remove(currmax)
                print(nums)
            