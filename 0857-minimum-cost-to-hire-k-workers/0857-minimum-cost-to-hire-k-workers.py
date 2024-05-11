import sys
import heapq
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers=[]
        for i in range(len(quality)):
            workers.append([wage[i]/quality[i] , quality[i]])
        
        workers.sort(key=lambda x:(x[0]))
        print(workers)
        totalpay=sys.maxsize
        qualitysum=0
        priorityQueue=[]
        for i in workers:
            ratio=i[0]
            qualitysum+=i[1]
            heapq.heappush(priorityQueue,-(i[1]))
            if len(priorityQueue)>k:
                
                poped=heapq.heappop(priorityQueue)
                # as poped in -ve value,to subtract from qualitysum ,we need to add this
                qualitysum+=poped
            if len(priorityQueue)==k:
                subtotalpay=qualitysum*ratio
                totalpay=min(totalpay,subtotalpay)
            print(qualitysum)

        return totalpay

        