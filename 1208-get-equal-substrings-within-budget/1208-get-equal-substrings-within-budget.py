class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost = []
        length = 0
        for i, j in zip(s, t):

            diff = abs(ord(i) - ord(j))
            cost.append(diff)
        i = 0
        j = 0
        sum = 0
        Max = 0

        while j < len(cost) and i < len(cost):
            sum += cost[j]

            if sum > maxCost:
                sum -= cost[i] + cost[j]

                i += 1

            else:

                Max = max(Max, j - i + 1)

                j += 1

        return Max
