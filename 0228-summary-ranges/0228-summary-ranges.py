class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result=[]
        i=0
        j=0
        while(i<len(nums)):
            j=i
            if (j+1)<len(nums):
                print(j+1)
                if nums[j]==nums[j+1]-1:
                    while((j+1)<len(nums) and nums[j]==nums[j+1]-1):
                    
                        j+=1
                    ans=f"{nums[i]}->{nums[j]}"
                    result.append(ans)
                    i=j+1
                else:
                    result.append(str(nums[i]))
                    i+=1
            else:
                result.append(str(nums[i]))
                i+=1
                
        return result
        