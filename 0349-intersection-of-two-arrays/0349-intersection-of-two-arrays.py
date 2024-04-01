class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection=[]
        for i in nums1:
            for j in nums2:
                if i==j:
                    intersection.append(i)
        
        
        interset=set(intersection)
        return interset