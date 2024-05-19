from typing import List
import sys

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        totalsum = 0
        minloss = sys.maxsize
        count = 0

        for value in nums:
            xor_value = value ^ k
            if xor_value > value:
                totalsum += xor_value
                count += 1
            else:
                totalsum += value
            minloss = min(minloss, abs(xor_value - value))

        if count % 2 == 0:
            return totalsum
        else:
            return totalsum - minloss

        
        if count%2==0:
            return totalsum
        return (totalsum-minloss)

                
