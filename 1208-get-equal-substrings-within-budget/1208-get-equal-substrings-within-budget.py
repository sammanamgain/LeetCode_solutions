class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost=[]
        length=0
        for i , j in zip(s,t):
            print(ord(i),ord(j))
            diff=abs(ord(i)-ord(j))
            cost.append(diff)

       # print("printing cost before sorting",cost)
        
        #cost.sort()
        print(cost)
        i=0
        j=0
        sum=0
        Max=0
        original=maxCost
        while(j<len(cost) and i<len(cost)):
            sum+=cost[j]
            print(sum,maxCost)
            if sum>maxCost:
                sum-=(cost[i]+cost[j])
                print(sum)
                i+=1
                
            else:
                print("entered in else block")

                Max=max(Max,j-i+1)
                print(Max)
                j+=1
                
        return Max




        