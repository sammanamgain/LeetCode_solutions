class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.answer = []
        self.calculatesum(candidates, [], 0, target)
        return self.answer

    def calculatesum(self, candidates, temp, i, sum):
        if sum < 0:
            return
        elif sum == 0:
            self.answer.append(temp[:])
            return
        elif i == len(candidates):
            return

        temp.append(candidates[i])
        self.calculatesum(candidates, temp, i, sum - candidates[i])
        temp.pop()
        self.calculatesum(candidates, temp, i + 1, sum)