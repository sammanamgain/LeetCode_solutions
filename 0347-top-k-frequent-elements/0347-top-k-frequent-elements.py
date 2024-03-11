class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        print(nums,k)
        hashmap={}
        for i in nums:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        length=len(nums) + 1
        bucket=[[] for _ in range(length)]

        for key,value in hashmap.items():
           # print(key,value)
     
            bucket[value].append(key)
            #print(bucket)
        print("bucket",bucket)
        
        final=[]
        length-=1
        
        
        while(k>0 and len(bucket)>0):
            
            print('length',length)
            print('bucket length',len(bucket))
            print(bucket[length])
            if len(bucket[length]) == 0:
                bucket.pop()
                pass
            else:
                ele=bucket.pop()
                final.extend(ele)
                k=k-len(ele)
                
            length-=1
            
        print(final)
        return final
            