def binary_search(l,low,high,k):
    while(low<=high):
        mid=(low+high)//2
        if (l[mid]==k):
            return mid 
        elif (l[mid]>k):
            high=low-1 
        else:
            low=mid+1 
    return -1

l=[4,3,6,7,8,1,2]
l.sort()
low=0
high=len(l)
k=8
s=binary_search(l,low,high,k)

if s==-1:
    print(k,"Is not Presented in this list")
else:
    print(k,'Is find in place of :',s)