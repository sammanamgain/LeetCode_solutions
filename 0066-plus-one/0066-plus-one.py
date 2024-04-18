class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i=len(digits)-2
        carry=0
        sum=digits[-1]+1
        remainder=sum%10
        carry=sum//10

        digits[-1]=remainder
        if len(digits)==1:
            if carry!=0:
                digits=[carry]+digits[::]
            return digits
            

        

        while carry!=0:
            print(i)
            if i==0:
                sum=digits[i]+carry
                remainder=sum%10
                carry=sum//10
                digits[i]=remainder
                if carry!=0:
                    digits=[carry]+digits[::]
                    break
                break
            else:
                sum=digits[i]+carry
                remainder=sum%10
                carry=sum//10
                digits[i]=remainder
                i-=1
        return digits


        