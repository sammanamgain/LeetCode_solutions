class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=len(nums)-1
        copy=list(nums)
        nums.sort()
        while(i<len(nums) and j<len(nums)):
          
        
            sum=nums[i]+nums[j]

            if(sum==target):
                temp=[]

                for k in range(len(copy)):
                    if (copy[k]==nums[i] or copy[k]==nums[j]):
                       
                        temp.append(k)

                return temp
            if(sum>target):
                j-=1
            if(sum<target):
                i+=1
        