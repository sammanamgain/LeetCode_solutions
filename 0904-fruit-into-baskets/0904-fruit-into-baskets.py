class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        Max=0
        left=0
        right=0
        hashmap={}
        while(right<len(fruits) and left<len(fruits)):
            print(Max)
            if fruits[right] in hashmap:
                hashmap[fruits[right]]+=1
                if len(hashmap)>2:
                     print("does length exceed")
                     hashmap[fruits[left]]=hashmap[fruits[left]]-1
                     if hashmap[fruits[left]]==0:
                         hashmap.pop(fruits[left])
                     left+=1
                     if (len(hashmap) <2):
                         Max=max(Max,right-left+1)
                     right+=1
                else:

                    Max=max(Max,right-left+1)
                    right+=1
                
            else:
                hashmap[fruits[right]]=1
                if len(hashmap)>2:
                    print("does length exceed")
                    hashmap[fruits[left]]-=1
                    if hashmap[fruits[left]]==0:
                        hashmap.pop(fruits[left])
                    left+=1
                    if (len(hashmap) <2):
                        Max=max(Max,right-left+1)
                    right+=1
                    
                    
                else:
                    Max=max(Max,right-left+1)
                    right+=1
                
                
        return Max
                

        