def bubble_sort(l):
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if (l[j]>l[j+1]):
                l[j],l[j+1]=l[j+1],l[j]
    return l 
l=[3,2,5,4,1]
print(bubble_sort(l))


# Iteration 1st= i=0 
#                j=n-0-1=4
#                3 2 5 4 1 
#                3>2  2,3    2,3,5,4,1
#                3>5  no     2,3,5,4,1
#                5>4  4,5    2,3,4,5,1
#                5>1  1,5    2,3,4,1,5

# After each iteration maximum value swap the last position 
# 1st iteration - 5
# 2st iteration - 4
# 3st iteration - 3
# 4st iteration - 2
# 5st iteration - 1


