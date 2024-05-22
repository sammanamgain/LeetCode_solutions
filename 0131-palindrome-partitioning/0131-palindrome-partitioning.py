class Solution:
    def partition(self, s: str):
        res = []
        path = []
        self.func(0, s, path, res)
        return res
    
    def func(self, index: int, s: str, path: list, res: list):
        if index == len(s):
            res.append(path[:])
            return
        for i in range(index, len(s)):
            if self.isPalindrome(s, index, i):
                path.append(s[index:i + 1])
                self.func(i + 1, s, path, res)
                path.pop()
    
    def isPalindrome(self, s: str, start: int, end: int):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
