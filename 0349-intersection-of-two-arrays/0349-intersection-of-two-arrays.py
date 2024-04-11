class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection=[]
        nums1=set(nums1)
        nums2=set(nums2)
        
        for j in nums2:
            if j in nums1:
                intersection.append(j)
        
        
        
        return intersection