class Solution:
    def __init__(self):
        self.result=[]
        self.validword=set()


    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.validword=set(wordDict)
        
        self.findsentence(0,"",s)
        print(self.result)
        return self.result
    
    def findsentence(self,i,currSentence,s):

        # base case
        if i==len(s):
            self.result.append(currSentence)

            return
        temp=""
        while(i<len(s)):
            temp+=s[i]
            original=currSentence
            if temp in self.validword:
                # find next word:
                if len(currSentence)!=0:
                    currSentence+=" "
                currSentence+=temp
                self.findsentence(i+1,currSentence,s)
            currSentence=original

                # explore more
            i+=1

        return


