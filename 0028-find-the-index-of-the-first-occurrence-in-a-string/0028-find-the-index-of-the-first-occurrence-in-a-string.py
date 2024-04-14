class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l=0
        n=len(needle)
        for i in range(len(haystack)):
            strrange=i+n
            print(haystack[i:strrange])
            if haystack[i:strrange]==needle:
                return i

        return -1
        
        