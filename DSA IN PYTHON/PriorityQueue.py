class Priority_Queue:
    def __init__(self):
        self.item=[]
    def is_empty(self):
        return len(self.item)==0
    
    def push(self,data,priority):
        i=0
        n=len(self.item)
        while i<n and self.item[i][1]<=priority:
            i+=1
        self.item.insert(i,(data,priority))

        print(self.item)
    def pop(self):
        if not self.is_empty():
            return self.item.pop(0)[0]
        else:
            return "No element are there"
    
    def size(self):
        if not self.is_empty():
            return len(self.item)
    


p=Priority_Queue()
p.push(10,1)
p.push(30,3)
p.push(20,2)
print(p.pop())
print(p.size())

        

