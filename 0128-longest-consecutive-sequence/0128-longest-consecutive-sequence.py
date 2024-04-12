class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we can easily do by sorting , but we need to do in O(n) complexity
        #  we will find the smallest number of sequence
        # like in example 1, 1, 100 and 200 are smallest number of their corresponding sequence
        # we find this just by iterating once,for 1,if there exits 0 or not, if left neighbour exists ,it is not starting point
        # else it is ,then check 2,3,4,etc, but while iterating ,skip 2,3,as they  have left neighbour
        # we need search for 0,2 in case of 1, so we use set using which do in O(1) time complexity
        numset=set(nums)
        Max=0
        
        for i in nums:
            if i-1 not in numset:
                count=0
                while (i+count) in numset:
                    count+=1
                Max=max(Max,count)

                
                
        return Max
                    



