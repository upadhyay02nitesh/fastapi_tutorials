class Queue:
    def __init__(self) :
        self.queue=[]
    def EnqueueFirst(self,item):
        self.queue.insert(0,item)
    def EnqueueLast(self,item):
        self.queue.append(item)
    def isEmpty(self):
        if (len(self.queue))==0:
            return True
    def DequeueFirst(self):
        if(self.isEmpty()):
            print("Underflow condition")
        else:
            self.queue.pop(0)
    def DequeueLast(self):
        if(self.isEmpty()):
            print("Underflow condition")
        else:
            self.queue.pop()
    def display(self):
        print(self.queue)
    
s=Queue()
s.EnqueueFirst(10)
s.EnqueueLast(20)
s.EnqueueFirst(30)
s.display()
s.DequeueLast()
s.display()
s.DequeueFirst()
s.display()

s.DequeueLast()
s.display()
s.DequeueFirst()