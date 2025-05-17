class Stack:
    def __init__(self,capacity):
        self.stack=[]
        self.capacity=capacity

    def is_empty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return IndexError("No element are there")
    
    
    def push(self,data):
        if self.size()<self.capacity:
            self.stack.append(data)
        else:
            return "Overflow Condition"
    def display(self):
        print(self.stack)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "underflow Condition"
    
s=Stack(4)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.peek())
s.display()


    

