import heapq
def Heap_sort(l):
    s=[]
    heapq.heapify(l)
    for i in range(len(l)):
        s.append(heapq.heappop(l))
    return s

l=[3,4,6,2,6,8,2,5]
print(Heap_sort(l))
