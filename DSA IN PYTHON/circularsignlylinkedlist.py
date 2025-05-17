class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=None
    
class CSLL:
    def __init__(self):
        self.last=None 
    
    def is_empty(self):
        return self.last==None 
    
    def insert_first(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n 
            self.last=n 
        else:
            n.next=self.last.next
            self.last.next=n
            self.last = n
    def insert_last(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n 
            self.last=n 
        else:
            n.next=self.last.next 
            self.last.next=n
            self.last=n
    def insert_particular(self,pos,data):
        temp=self.last.next 
        n=Node(data)
        while temp!=self.last:
            if temp.item==pos:
                break
            temp=temp.next 
      
        if temp==self.last:
                n.next=temp.next 
                temp.next=n
                self.last=n
        else:
            n.next=temp.next 
            temp.next=n
    
    def delete_first(self):
        if not self.is_empty():
            if self.last.next==self.last:
                self.last=None 
            else:
                self.last.next=self.last.next.next
    
    def delete_last(self):
        if not  self.is_empty():
            if self.last.next==self.last:
                self.last=None 
            else:
                temp=self.last.next 
                while temp.next!=self.last:
                    temp=temp.next 
                temp.next=self.last.next 
                self.last=temp 
    
    def delete_particular(self, data):
        if not self.is_empty():
            if self.last.next == self.last:  # Only one node
                if self.last.item == data:
                    self.last = None
            else:
                temp = self.last.next
                prev = None

                while temp != self.last:
                    if temp.item == data:
                        if temp == self.last.next:  # If the node to delete is the first node
                            self.last.next = temp.next
                            del temp
                            return
                        else:  # If the node to delete is in between
                            prev.next = temp.next
                            del temp
                            return
                    prev = temp
                    temp = temp.next

            # Check if the last node is to be deleted
                temp=self.last.next 
                while temp.next!=self.last:
                    temp=temp.next 
                temp.next=self.last.next 
                self.last=temp 


    def search(self,data):
        if self.is_empty():
            return None
        else:
            temp=self.last.next 
            while temp!=self.last:
                if temp.item==data:
                    return True
                temp=temp.next
            if temp.item==data:
                return True
            return False 
    
    def display(self):
        temp=self.last.next 
        while temp!=self.last:
            print(temp.item,end=" ")
            temp=temp.next 
        print(temp.item,end=" ")
    


s=CSLL()
s.insert_first(1)
s.insert_last(2)
print(s.search(2))
s.insert_particular(2,3)
s.insert_last(4)
s.display()
print()
s.delete_first()
s.display()
print()
s.delete_last()
s.display()
s.delete_particular(2)
print()
s.display()

        