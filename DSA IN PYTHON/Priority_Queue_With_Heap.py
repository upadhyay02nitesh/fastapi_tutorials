import heapq

data=[]
for i in range(3):
    n=int(input("Enter the Roll number :"))
    m=input("Enter the Name :")
    heapq.heappush(data,(n,m))
print(data)
print("Minimu Priority Element --")
for i in range(len(data)):
    print(heapq.heappop(data))