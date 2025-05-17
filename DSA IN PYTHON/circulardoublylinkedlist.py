class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item=item
        self.prev=None 
        self.next=None
    
class CDLL:
    def __init__(self):
        self.start=None 
    
    def is_empty(self):
        return self.start==None 
    
    def insert_first(self,data):
        n=Node(data)
        if  self.is_empty():
            n.next=n 
            n.prev=n 
            self.start=n 
        else:
            n.next=self.start
            n.prev=self.start.prev 
            self.start.prev.next=n
            self.start.prev=n 
            self.start=n
    def insert_last(self,data):
        n=Node(data)
        if  self.is_empty():
            n.next=n 
            n.prev=n 
            self.start=n
        else:
            n.next=self.start 
            n.prev=self.start.prev 
            self.start.prev.next=n 
            self.start.prev=n 
    def insert_particular(self,pos,data):
        if not self.is_empty():
            n=Node(data)
            temp=self.start
        if temp is not None:
            if temp.item==pos:
        
                n.next=temp.next 
                n.prev=temp 
                temp.next.prev=n 
                temp.next=n 
            else:    
                temp=temp.next
        
                while temp!=self.start:
                    if temp.item==pos:
                        break
                    temp=temp.next
                n.next=temp.next 
                n.prev=temp 
                temp.next.prev=n 
                temp.next=n
           

            

    def search(self,data):
        temp=self.start
        if temp is not None:
            if temp.item==data:
                return True
            else:
                temp=temp.next
                while temp!=self.start:
                    if temp.item==data:
                        return True
                    temp=temp.next
        return False

    def delete_first(self):
        if not self.is_empty():
            if self.start.prev==self.start.next:
                self.start=None
            else:
                self.start.next.prev=self.start.prev 
                self.start.prev.next=self.start.next
                self.start=self.start.next 
                temp=None
    
    def delete_last(self):
        if not self.is_empty():
            if self.start.prev==self.start.next:
                self.start=None
            else:
                self.start.prev.prev.next=self.start
                self.start.prev=self.start.prev.prev

  

    
    def display(self):
        temp=self.start
        if temp is not None:
            print(temp.item,end=" ")
            temp=temp.next
        while temp!=self.start:
            print(temp.item,end=" ")
            temp=temp.next
    
    





s=CDLL()
s.insert_first(10)
s.insert_first(20)
s.insert_first(30)
print()
# s.insert_particular(20,100)
print(s.search(20))

s.display()
print()
s.delete_last()
s.display()
print()
s.delete_first()
s.display()