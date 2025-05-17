class Node:
    def __init__(self,item=None,prev=None,next=None) :
        self.item=item
        self.prev=prev
        self.next=next 
    
class Dequeue_DLL:
    def __init__(self) :
        self.front=None
        self.rear=None
        self.item_count=0

    
    def is_empty(self):
        return self.front==None 
    
    def insert_first(self,item):
        n=Node(item)
        if self.is_empty():
            self.front=n 
            self.rear=n
        else:
            n.next=self.front 
            self.front.prev=n 
            self.front=n 
        self.item_count+=1
        


    def insert_last(self,item):
        n=Node(item)
        if self.is_empty():
            self.front=n 
            self.rear=n
        else:
            self.rear.next=n
            n.prev=self.rear
            self.rear=n
        self.item_count+=1
       
    def delete_first(self):
        if not self.is_empty():
            if self.rear==self.front:
                self.front=None
                self.rear=None
            else:
                self.front.next.prev=None 
                self.front=self.front.next
            self.item_count-=1
            
        else:
            print("No element found to delete")
    def delete_last(self):
        if not self.is_empty():
            if self.rear==self.front:
                self.front=None
                self.rear=None
            else:
                self.rear.prev.next=None 
                self.rear=self.rear.prev
            self.item_count-=1
            
        else:
            print("No element found to delete")
    def get_front(self):
        if not self.is_empty():
            print(self.front.item)
        else:
            print("No element")
    def get_rear(self):
        if not self.is_empty():
            print(self.rear.item)
        else:
            print("No element")
    



    

d=Dequeue_DLL()
d.insert_first(1)
d.insert_first(10)
d.get_front()
d.insert_last(100)
d.insert_last(140)
d.delete_last()
d.delete_first()
d.get_front()
print()
d.get_rear()
# print(d.item_count)




       