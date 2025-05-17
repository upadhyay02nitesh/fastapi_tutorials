class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item 
        self.next=next 
class DLL:
    def __init__(self):
        self.start=None

    def is_empty(self):
        return self.start==None 
    
    def insert_start(self,data):
        n=Node(None,data,self.start)
        if not self.is_empty():
            self.start.prev=n 
        self.start=n 

    def insert_last(self,data):
        
        if self.is_empty():
            self.start=Node(None,data,None)
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            n=Node(temp,data,None)
            temp.next=n 
    def insert_part(self,data,pos):
        temp=self.start
        while temp!=None:
            if temp.item==pos:
                break
            temp=temp.next
        n=Node(temp,data,temp.next)
        temp.next=n 


    def search(self,data):
        temp=self.start
        while temp!=None:
            if temp.item==data:
                return True
            temp=temp.next
        return False
    
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
            self.start.prev=None
    
    def delete_last(self):
        if self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next!=None :
                temp=temp.next
            temp.prev.next=None
            temp=None
    
    def delete_parti(self,pos):
        
        if self.start.next==None:
            if self.start.item==pos:
                self.start=None
        else:
            temp=self.start
            while temp!=None:
                if temp.item==pos:
                    break
                temp=temp.next
        
            if temp.next==None:
                temp.prev.next=None
                temp=None
            else: 
                temp.next.prev=temp.prev 
                temp.prev.next=temp.next 
                temp=None
                
    
    def display(self):
        temp=self.start
        while temp!=None:
            print(temp.item,end=" ")
            temp=temp.next
d=DLL()
d.insert_start(10)
d.display()
print()
d.insert_start(5)
d.display()
print()
d.insert_last(20)
d.display()
print()
d.insert_part(200,5)
d.display()
print()
# print(d.search(200))
# print()
print("****")
d.delete_last()
d.display()
print()
# d.display()
# print()
d.delete_first()
d.display()
print()
d.delete_parti(10)
d.display()
print()