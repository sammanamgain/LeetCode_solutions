class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        fractioncollection=[]
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                fractioncollection.append([arr[i],arr[j]])
        fractioncollection.sort(key=lambda x:x[0]/x[1] )
        return fractioncollection[k-1]

        