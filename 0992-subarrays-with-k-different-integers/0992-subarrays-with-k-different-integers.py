class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # we modify problem into like this
        # find the all number of subarrray under <=k
        # subarray with k distint integer= (<=k - <=k-1)

        def subarray(k):
            l=0
            r=0
            hashmap={}
            count=0
      
            while(r<len(nums)):
                if nums[r] in hashmap:
                    hashmap[nums[r]]+=1
                else:
                    hashmap[nums[r]]=1
                
                
                if len(hashmap)>k:
              
                    while(len(hashmap)>k):
                        hashmap[nums[l]]-=1
                        
                        if hashmap[nums[l]]==0:
                            hashmap.pop(nums[l])
                   
                        l+=1
                if len(hashmap)<=k:
                    count+=(r-l+1)
             
                r+=1
           

            return count

        return subarray(k)-subarray(k-1)


        