class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #selection sort
        # for i in range(len(nums)-1):
        #     min=i
        #     for j in range(i,len(nums)):
        #         if nums[j]<nums[min]:
        #             min=j
                
        #     temp=nums[i]
        #     nums[i]=nums[min]
        #     nums[min]=temp
        # return nums

        #merge sort

        self.divideandmerge(nums,0,len(nums)-1)
        return nums


    def divideandmerge(self,nums,left,right):
        if left>=right:
            return
        mid=(left+right)//2
        self.divideandmerge(nums,left,mid)
        self.divideandmerge(nums,mid+1,right)
        self.merge(nums,left,mid,right)
    def merge(self,arr,left,mid,right):
        #we are dividing logically ,hence to track we need to mid pointer too
        low=left
        high=mid+1
        temp=[]
        while(low<=mid and high<=right):
            if arr[low]<=arr[high]:
                temp.append(arr[low])
                low+=1
            else:
                temp.append(arr[high])
                high+=1
        while(low<=mid):

            temp.append(arr[low])
            low+=1
        while(high<=right):
            temp.append(arr[high])
            high+=1

        print(len(arr),len(temp))
        for i in range(left,right+1):
            arr[i]=temp[i-left]
        return



  

        