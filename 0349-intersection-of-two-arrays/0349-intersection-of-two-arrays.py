class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection=[]
        nums1=set(nums1)
        nums2=set(nums2)
        for i in nums1:
            for j in nums2:
                if i==j:
                    intersection.append(i)
        
        
        
        return intersection