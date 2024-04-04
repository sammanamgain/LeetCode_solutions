class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        sorted=[None]*len(nums)
        posindex=0
        negindex=1


        for i in nums:
            if(i>0):
                sorted[posindex]=i
                posindex+=2
            else:
                sorted[negindex]=i
                negindex+=2
        return sorted
            





        