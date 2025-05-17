import heapq
heap=[]
heapq.heappush(heap,40)
heapq.heappush(heap,70)
heapq.heappush(heap,10)
heapq.heappush(heap,90)
heapq.heappush(heap,60)
heapq.heappush(heap,30)
heapq.heappush(heap,50)
heapq.heappush(heap,20)
heapq.heappush(heap,80)

print("Min heap :",heap)

print("Min value in heap :",heapq.heappop(heap))

print("Min heap :",heap)





print("Covert any Binary tree to min heap")
l=[40,70,10,90,60,30,50,20,80]
heapq.heapify(l)
print(l)

print("Two samllest value")
print(heapq.nsmallest(2,l))

print("Two Largest value")
print(heapq.nlargest(2,l))