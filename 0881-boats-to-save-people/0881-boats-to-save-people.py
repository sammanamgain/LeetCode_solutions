class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count=0
        i=0
        while(i<len(people)):
            sum=people[i]
            while(sum<=limit):
                
                i+=1
                if i<len(people):
                    sum+=people[i]
                else:
                    break

            print(i)
            count+=1
            print(count)
            
        return count

        