class Queue:
    def __init__(self,capacity) :
        self.queue=[]
        self.capacity=capacity
    def isEmpty(self):
        return len(self.queue)==0
    def front(self):
        if not self.isEmpty():
            print(self.queue[0])
        else:
            print("No element")
    def rear(self):
        if not self.isEmpty():
            print(self.queue[-1])
        else:
            print("No element")
    def size(self):
        return len(self.queue)
    def Enqueue(self,item):
        if self.size()<self.capacity:
            self.queue.append(item)
        else:
            print("Overflow Condition")
    def Dequeue(self):
        if(self.isEmpty()):
            print("Underflow condition")
        else:
            self.queue.pop(0)
    def display(self):
        print(self.queue)
    
s=Queue(3)
s.Enqueue(10)
s.Enqueue(20)
s.Enqueue(30)
s.display()
s.Dequeue()
s.display()
s.Dequeue()
s.front()
print()
s.rear()
print()
s.display()
print(s.size())
s.Dequeue()

s.display()
s.Dequeue()