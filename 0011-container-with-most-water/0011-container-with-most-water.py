class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        Max=0
        while(l<=r):
            print(l,r)
            area=(r-l)*min(height[l],height[r])
            Max=max(Max,area)

            if height[l]>=height[r]:
                r-=1
            else:
                l+=1
        return Max