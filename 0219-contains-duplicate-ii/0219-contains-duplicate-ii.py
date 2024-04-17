class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap={}
        diff=0
        
        for i in range(len(nums)):
            if  nums[i] not in hashmap:
                hashmap[nums[i]]=i
            else:
                diff=abs(i-hashmap[nums[i]])
                
                if diff<=k:
                    return True
                hashmap[nums[i]]=i
                
                
        if diff==0:
            return False
        