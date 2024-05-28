class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        length = 0
        cost=[ abs(ord(i)-ord(j))  for i ,j in zip(s,t)]
        i = 0
        j = 0
        sum = 0
        Max = 0

        while j < len(cost) and i < len(cost):
            sum += cost[j]

            # if sum > maxCost:
            #     sum -= cost[i] + cost[j]

            #     i += 1

            while(sum>maxCost):
                sum-=cost[i]
                i+=1

            # else:

            Max = max(Max, j - i + 1)

            j += 1

        return Max
