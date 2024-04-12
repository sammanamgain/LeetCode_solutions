class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        Max=0

        while(r<len(prices)):
            if prices[r]-prices[l]>=0:
                Max=max(Max,prices[r]-prices[l])
                r+=1
            else:
                l+=1
        return Max
            
            

        