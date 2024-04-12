class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # using two pointer approach, one at left and another at right side
        l=0
        r=len(numbers)-1
        while(l<r):
            sum=numbers[l]+numbers[r]
            if sum==target:
                return [l+1,r+1]
            elif sum>target:
                r-=1
            else:
                l+=1
        
    
        