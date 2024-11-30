class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n  # If the length is <= 2, no need to process further.
        
        # `i` will be the index where the next unique or allowed duplicate element will be placed.
        i = 2
        for j in range(2, n):
            if nums[j] != nums[i - 2]:  # Compare with the element two positions behind.
                nums[i] = nums[j]
                i += 1
        
        return i
