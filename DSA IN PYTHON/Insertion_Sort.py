def insertion_sort(l):
    for i in range(1,len(l)):
        temp=l[i]
        j=i-1
        while j>=0 and temp<l[j]:
            l[j+1]=l[j]
            j-=1
        l[j+1]=temp
    return l


l=[4,3,2,1]
print(insertion_sort(l))

# Iteration-->1:
#     for(1,4):
#             i=1
#             j=i-1=0 
#             j>=0 and 3<4
#             l[j+1]=l[j]
#             l[1]=4 
#             j=j-1=0-1=-1
#             False
#             l[j+1]=l[-1+1]=l[0]=temp=3

# now list look like 3,4,2,1

# Iteration-->2:
#     for(1,4):
#             i=2
#             j=i-1=1
#             j>=0 and 2<4
#             l[j+1]=l[j]
#             l[2]=4 
#             j=j-1=1-1=0

#             j>=0 and 2<3
#             l[j+1]=l[j]
#             l[1]=3
#             j=j-1=0-1=-1

#             False
#             l[j+1]=l[-1+1]=l[0]=temp=2
# now list look like 2,3,4,1

# Iteration-->3:
#     for(1,4):
#             i=3
#             j=i-1=2
#             j>=0 and 1<4
#             l[j+1]=l[j]
#             l[3]=4 
#             j=j-1=2-1=1

#             j>=0 and 1<3
#             l[j+1]=l[j]
#             l[2]=3
#             j=j-1=1-1=0


#             j>=0 and 1<2
#             l[j+1]=l[j]
#             l[1]=2
#             j=j-1=0-1=-1

#             False


#             l[j+1]=l[-1+1]=l[0]=temp=1
# now list look like 1,2,3,4




