
# here front is always first then rear will increase if value inserted

# insert
# 1     front =1  rear=1 item=1
# 1 2   front =1  rear=2 item=2
# 1 2 3  front =1 rear=3 item=3

# delete 

# 1 2 3    front =1 rear=3 item=3
# 2 3      front =2 rear=3 item=3-1=2
# 3        front =3 rear=3 item=2-1=1


class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next 
    
class Queue_SLL:
    def __init__(self):
        self.front=None 
        self.rear=None 
        self.item_count=0
    
    def is_empty(self):
        return self.front==None 
    
    def enqueue(self,data):
        n=Node(data)
        if self.front==None:
            self.front=n 
            self.rear=n 
        else:
            self.rear.next=n 
            self.rear=n 
        self.item_count+=1
    
    def dequeue(self):
        if not self.is_empty():
            if self.rear==self.front:
                self.rear=None
                self.front=None
            else:
                self.front=self.front.next
            self.item_count-=1
            
        else:
            print("Underflow Condition")
    def get_front(self):
        if not self.is_empty():
            print(self.front.item)
        else:
            print("No element",self.front.item)
    def get_rear(self):
        if not self.is_empty():
            print(self.rear.item)
        else:
            print("No element",self.rear.item)
    def display(self):
        if not self.is_empty():
            temp=self.front
            while temp!=self.rear:
                print(temp.item,end=" ")
                temp=temp.next 
            print(temp.item,end=" ")
        else:
            print("No element")

q=Queue_SLL()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.get_front()
print()
q.get_rear()
print()
q.dequeue()
q.display()


        
    

        

   