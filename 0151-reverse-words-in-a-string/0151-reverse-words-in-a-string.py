class Solution:
    def reverseWords(self, s: str) -> str:
        splited_word=[]
        splited_word=s.split(' ')
        print(splited_word)

        ans=""
        firstelement=2
        for i in range(len(splited_word)-1,-1,-1):
           
                

        
            if splited_word[i]=='':
                pass
            elif firstelement==2 :
                
                ans=ans+splited_word[i]
                firstelement=3
            else:
                ans=ans+" "+splited_word[i]
        return ans
        

        