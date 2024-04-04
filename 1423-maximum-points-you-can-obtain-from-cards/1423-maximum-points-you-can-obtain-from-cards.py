class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left=k-1
        right=len(cardPoints)
        Max=0
        sum=0
        while(left>=-1):
            if left==k-1:
                for i in range(left+1):
                    sum+=cardPoints[i]
            if right<len(cardPoints):
                sum+=cardPoints[right]
            


            Max=max(Max,sum)
            sum-=cardPoints[left]
            left-=1
            right-=1
          
        return Max


            

        