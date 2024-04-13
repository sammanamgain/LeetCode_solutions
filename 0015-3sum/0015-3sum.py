class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        print(nums)
        nums.sort()
        print(nums)
        p=0
        
       
        result=[]
        while(p<len(nums)-2):
            print("value of p",p)
            q=p+1
            r=len(nums)-1

            while(q<=r and r>q):
                sum=0
                sum=nums[p]+nums[q]+nums[r]
                if sum==0:
                    result.append([nums[p],nums[q],nums[r]])
                    prev=nums[q]
                    q+=1
                    if q==r:
                        break
                
                    while(prev==nums[q]):
                        q+=1
                        if q==r:
                            break
                
                    
                elif sum>0:
                    r-=1
                else:
                    q+=1
            prev=nums[p]
            p+=1
           
            if p==len(nums)-2:
                    break
            while(prev==nums[p]):
                p+=1
                if p==len(nums)-2:
                    break
        return result

        





        