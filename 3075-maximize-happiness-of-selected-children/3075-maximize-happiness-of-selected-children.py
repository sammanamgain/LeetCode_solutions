class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        index=0
        n=len(happiness)-1
        Sum=0
        while(index!=k):
            Sum += (happiness[n - index] - index) if (happiness[n - index] - index) > 0 else 0
            index+=1

        return Sum


