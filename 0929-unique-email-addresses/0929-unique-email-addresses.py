class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        Email=set()
        for i in emails:
            firstpart,secondpart=i.split('@')
           
            pluscollection=firstpart.split('+')
            
            dotcollection=pluscollection[0].split('.')
        
            summationbefore="".join(dotcollection)
         
            uniqueemail=summationbefore+'@'+secondpart
      
            Email.add(uniqueemail)
          
        return len(Email)



        