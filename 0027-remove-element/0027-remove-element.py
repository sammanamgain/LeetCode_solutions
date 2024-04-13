class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        i=0
        while(i<len(nums)):
            print(k)
            if nums[i]==val:
                if len(nums)==1:
                    return k
                
                if i==len(nums)-1:
                    return k
                
                j=i+1
                print(i,j)
                
                while(nums[i]==nums[j]):
                    j+=1
                    if j==len(nums):
                        return k
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                i+=1
                k+=1
                
                
            else:
                k+=1
                i+=1
        print(k)
        return k
        