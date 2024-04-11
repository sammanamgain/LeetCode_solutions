class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        Email={}
        for i in emails:
            firstpart,secondpart=i.split('@')
           
            pluscollection=firstpart.split('+')
            
            dotcollection=pluscollection[0].split('.')
        
            summationbefore="".join(dotcollection)
         
            uniqueemail=summationbefore+'@'+secondpart
      
            if uniqueemail not in  Email:
                Email[uniqueemail]=1
            

          
        return len(Email)



        