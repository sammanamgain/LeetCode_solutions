class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # carry=0
        # sum=digits[-1]+1
        # remainder=sum%10
        # carry=sum//10

        # digits[-1]=digits[-1]+remainder

        # if carry!=0:

        number=""
        for i in digits:
            number+=str(i)
        intnum=int(number)
        intnum=intnum+1
        output=[]
        for i in str(intnum):
            output.append(int(i))
        return output




        