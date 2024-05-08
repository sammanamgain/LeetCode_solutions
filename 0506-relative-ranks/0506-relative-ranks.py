class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_array=sorted(score,reverse=True)
        hashmap={}
        index=0
        for i in sorted_array:
            hashmap[i]=index
            index+=1
        
        for i in range(len(score)):
            rank=hashmap[score[i]]
            if rank ==0:
                score[i]='Gold Medal'
            elif rank==1:
                score[i]='Silver Medal'
            elif rank==2:
                score[i]='Bronze Medal'
            else:
                score[i]=str(rank+1)
            
        return score

        