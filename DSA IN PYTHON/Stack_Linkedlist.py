
#insert start and delete start

# insert
# 2
# 3 2
# 4 3 2

# delete 
# 4
# 3
# 2

class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next 
    
class Stack_SLL:
    def __init__(self,start=None):
        self.start=None 
    def is_empty(self):
        return self.start==None
    
    def push(self,data):
        n=Node(data)
        if self.is_empty():
            self.start=n 
        else:
            n.next=self.start
            self.start=n 
    
    def peek(self):
        print(self.start.item)
    def size(self):
        i=0
        temp=self.start
        while temp!=None :
            i+=1
            temp=temp.next
        print(i)

    
    def pop(self):
        if not self.is_empty():
            self.start=self.start.next 
        else:
            return print("UnderFlow Condition")    
    def display(self):
        temp=self.start
        while  temp!=None:
            print(temp.item,end=" ")
            temp=temp.next 

s=Stack_SLL()
s.push(2)
s.display()
print()
s.push(3)
s.display()
print()
s.push(4)
print("Peek element")
s.peek()
print()
s.size()
print()
s.display()
print()

s.pop()
s.display()
print()
s.pop()
s.display()
print()
s.pop()
print()
s.pop()
s.display()
print()
s.size()


    
            
            


        