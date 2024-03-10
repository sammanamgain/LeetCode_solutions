class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for index,value in enumerate(nums):
            print(index,value)
            remaining=target-value
            if remaining in hashmap:
                firstindex=hashmap[remaining]
                return [index,firstindex]
            else:
                hashmap[value]=index
            
        