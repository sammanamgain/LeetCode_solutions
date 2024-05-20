class Solution:
    def __init__(self):

        self.sumlist=[]
    def subsetXORSum(self, nums: List[int]) -> int:
        sum=0
        sum=self.recursive_sum(nums,0,sum)
        sum=0
        print(self.sumlist)
        for i in self.sumlist:
            sum+=i
        return sum


    
    def recursive_sum(self,arr,i,sum):
     
        if i ==len(arr):
            self.sumlist.append(sum)
            return
                
        self.recursive_sum(arr,i+1,(sum^arr[i]))
        self.recursive_sum(arr,i+1,sum)
        return
            