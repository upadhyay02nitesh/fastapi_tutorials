class Node:
    def __init__(self,item=None,next=None):
        self.item=item 
        self.next=next 

class SLL:
    def __init__(self):
        self.start=None 
    
    def isEmpty(self):
        return self.start==None 
    
    def insert_start(self,data):
        n=Node(data,self.start)
        self.start=n
    
    def insert_last(self,data):
        n=Node(data,None)

        if self.isEmpty():
            self.start=n 
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next 
            temp.next=n

    def search(self,data):
        temp=self.start 
        while temp!=None:
            if temp.item==data:
                return temp 
            temp=temp.next
    
    def insert_particular(self,data,val):
        temp=self.start
        while temp!=None:
            if temp.item==data:
                break
            temp=temp.next
        temp.next=Node(val,temp.next)
            


    def delete_first(self):
        self.start=self.start.next

    def delete_last(self):
        if self.start.next==None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next!=None:
                temp=temp.next
              
            temp.next=None

    def delete_particular(self,data):
        if self.start.next is None:
            if self.start.item==data:
                self.start=None
        else:
            temp=self.start
            while temp!=None:
                if temp.item==data:
                    break
                prev=temp
                temp=temp.next 
            prev.next=temp.next
            temp=None
            
    
    def display(self):
        temp=self.start
        while temp!=None:
            print(temp.item,end=" ")
            temp=temp.next 

    

s=SLL()
# print(s.isEmpty())
s.insert_start(1)
s.insert_start(2)
s.insert_last(3)
s.insert_particular(1,4)

s.display()
print()
# print(s.isEmpty())
# print(s.search(2))
# s.display()
# s.delete_first()
# print()
# s.display()
print()
s.delete_last()
print()

s.display()
# s.delete_particular(4)
# print()
# s.display()       
        