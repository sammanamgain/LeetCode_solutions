class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index=0
        for i in range(len(word)):
            if word[i] ==ch:
                index=i
                break
        
        if index==0:
            return word
     
      
        revstr=''.join(reversed(list(word[0:index+1])))
        
        
        
        return revstr+word[index+1:]
        
          
        