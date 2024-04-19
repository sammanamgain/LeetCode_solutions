class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while(l<=r):
            print(l,r)
            m=(l+r)//2
            print(m)
            if nums[m]==target:
                return m
            elif l==r:
                if nums[l]>target:
                    return l
                else:
                    return l+1
            elif nums[m]<target:
                l=m+1
            else:
                r=m-1
                if r<0:
                    return m
            
        return r+1
            
       



        