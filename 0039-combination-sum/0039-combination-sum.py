class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        self.answer=[] # 2d list
        self.calculatesum(candidates,[],i=0,sum=target)
        return self.answer

    def calculatesum(self,candidates,temp,i,sum):
        print(temp)
        print(i)
        print(sum)

        #best case
        if sum==0:
            print(temp)
            self.answer.append(temp[::])
            return 
        
        if i==len(candidates):
            return 
        if  sum<candidates[i]:
            return

        #lets take i
        temp.append(candidates[i])
        sum-=candidates[i]
        self.calculatesum(candidates,temp,i,sum)
        temp.pop()
        sum+=candidates[i]
        # lets not take i
        self.calculatesum(candidates,temp,i+1,sum)
