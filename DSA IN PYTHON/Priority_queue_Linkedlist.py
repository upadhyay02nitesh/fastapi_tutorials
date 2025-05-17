class Node:
    def __init__(self,item=None,prior=None,next=None) :
        self.item=item 
        self.prior=prior
        self.next=next 
class Prior_SLL:
    def __init__(self):
        self.start=None 
        self.item_count=0
    
    def is_empty(self):
        return self.start==None
    
    def push(self, data, prior):
    
        n = Node(data, prior)
        if self.is_empty() or prior <= self.start.prior:
            n.next = self.start
            self.start = n
        else:
            temp = self.start
            while temp.next is not None and temp.next.prior <= prior:
                temp = temp.next
            n.next = temp.next
            temp.next = n
        self.item_count += 1
    def pop(self):
        if not self.is_empty():
            self.start=self.start.next 
            self.item_count-=1
        else:
            print("No element are there for deletion")



                
    def display(self):
        if not self.is_empty():
            temp=self.start
            while temp!=None:
                print(temp.item,end=" ")
                temp=temp.next
p=Prior_SLL()
p.push(10,1)
p.push(106,3)
p.push(130,2)
p.pop()
print()
p.display()
print()
print() 
print(p.item_count)
p.pop()
p.display()


        
        
