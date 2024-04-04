class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        ele=nums[0]
        count=0
        for i in nums:
            if (ele==i):
                count+=1
            else:
                count-=1
            if count==0:
                ele=i
                count=1
        
        #verify the count
        finalcount=0
        for i in nums:
            if (i==ele):
                finalcount+=1
        print(ele)
        if(finalcount>len(nums)//2):
            return ele
        else:
            return 0