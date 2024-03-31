class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        two=cost[-1]
        one=cost[len(cost)-2]
        for i in range(len(cost)-3,-1,-1):
            temp=one
            one=min(cost[i]+one,cost[i]+two)
            two=temp
        return min(one,two)