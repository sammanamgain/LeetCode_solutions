class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count=0
        l=0
        r=0
        odd=0
        firstodd=[]
        while(r<len(nums)):
            if nums[r]%2!=0:
                odd+=1
                firstodd.append(r)
            # below code also work but i making more optimal , as we donot need to traverse again
            # while(odd>k):
            #     if nums[l]%2!=0:
            #         odd-=1
            #         firstodd=firstodd[1:]
            #     l+=1
            # no need to transverse one by one
            if odd>k:
                l=firstodd[0]+1
                odd-=1
                firstodd=firstodd[1:]
            if odd==k:
                count+=1
                count+=firstodd[0]-l

            r+=1

        return count
 
