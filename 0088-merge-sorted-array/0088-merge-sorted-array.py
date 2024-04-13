class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # we will start from filling the array from backwards
        length=len(nums1)-1
        l=m-1
        r=n-1
        while(l>=0 and r>=0):
            
            if nums1[l]>=nums2[r]:
                nums1[length]=nums1[l]
                l-=1
                length-=1
            else:
                nums1[length]=nums2[r]
                r-=1
                length-=1
        while(r>=0):
            nums1[r]=nums2[r]
            r-=1

        
        

        