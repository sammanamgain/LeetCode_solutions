class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max=0
        count=0
        for i in nums:
            if i ==1:
                count=count+1
            else:
                count=0
            if count>max:
                max=count
        return max