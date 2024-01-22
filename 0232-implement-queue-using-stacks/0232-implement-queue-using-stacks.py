class MyQueue:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        

    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self) -> int:
        if(len(self.stack2)==0):
            if(len(self.stack1)==0):
                return 'stack is empty'
            else:
              
                for i in range(0,len(self.stack1)):
                    temp=self.stack1.pop()
               
                    self.stack2.append(temp)
           
                
                popedvalue=self.stack2.pop()
           
                for i in range(0,len(self.stack2)):
                    temp=self.stack2.pop()
                    self.stack1.append(temp)
                return popedvalue
            
                    
                
        

    def peek(self) -> int:
        if(len(self.stack1)==0):
            return "Empty"
        else:
             return self.stack1[0]
        

    def empty(self) -> bool:
        if(len(self.stack1)==0):
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()