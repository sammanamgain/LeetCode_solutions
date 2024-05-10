class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        collectionSet=set()
        n=len(nums)

        def subset(nums,i,n,temp):
            if i==n:
                collectionSet.add(tuple(sorted(temp)))
                return 

            temp.append(nums[i])
            
            subset(nums,i+1,n,temp)
            if temp:
                temp.pop()
            
            subset(nums,i+1,n,temp)
            return
        subset(nums,0,n,[])
        return list(collectionSet)


         


            

            
        