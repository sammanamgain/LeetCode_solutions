class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        hashmap={}
        for i in nums:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        Max=-1
        frequent=-1
        for key,values in hashmap.items():
            if values>Max:
                Max=max(Max,values)
                frequent=key
            
        return frequent

        