class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0,len(nums)+1):
            count=0
            for j in nums:
                if j>=i:
                    count+=1
            if count==i:
                return i
        return  -1
            


        