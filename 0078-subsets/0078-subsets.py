class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # using recursion
        # subset is formed by either including or excluding element from list(left to right)
        # like include 1 ([1]),exclude 1([]),include 2([1,2]),exclude 2([1])

        self.answer = []  # it will be 2d array
        temp = []
        self.generatesubset(nums, temp, 0)

        return self.answer

    def generatesubset(self, nums, temp, i):

        # either i will take i or ignore i

        if i == len(nums):

            self.answer.append(temp[::])
            
            return
        #  take i
        temp.append(nums[i])

        self.generatesubset(nums, temp, i + 1)
   # lets not take i
        temp.pop()
        self.generatesubset(nums, temp, i + 1)

     

        return
