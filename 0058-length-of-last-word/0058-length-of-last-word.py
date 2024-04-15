class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split(" ")
  
        lastindex=-1
        while(lastindex>=(-len(s))):
            if s[lastindex].isalpha():
                print(s[lastindex])
                return len(s[lastindex])
            else:
                lastindex-=1

        
        