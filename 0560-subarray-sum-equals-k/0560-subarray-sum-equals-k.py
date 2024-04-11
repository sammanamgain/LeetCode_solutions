class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
      # this appraoch is based on prefix sum
      # we know the sum of prefix sum=s
      # we know value of k , if there is s-k , in previous sum( we keep this using hashmap) , then k exists increment count 
        count = 0
        hashmap = {}
        hashmap[0]=1
        sum = 0
        for i in nums:
            print(i)
            sum += i
            print("printing sum till now",sum)
            diff = sum - k
            print("printing differences",diff)
            if diff in hashmap:
                print("yes diff")
                count += hashmap[diff]
            if sum in hashmap:
                hashmap[sum]+=1
            else:
                hashmap[sum]=1
            print(hashmap)
        return count



        