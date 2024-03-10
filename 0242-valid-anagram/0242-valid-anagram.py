class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        orders="".join(sorted(s))
        ordert="".join(sorted(t))
        if(orders==ordert):
            return True
        return False
        