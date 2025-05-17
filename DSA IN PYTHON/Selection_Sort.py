def selection_sort(l):
    n=len(l)
    for i in range(n-1):
        for j in range(i+1,n):
            if(l[i]>l[j]):
                l[i],l[j]=l[j],l[i]
    return l 
    
l=[3,2,5,4,1]
print(selection_sort(l))


# Iteration 1st= i=0 
#                j=i+1=0
#                3 2 5 4 1 
                #  3>2 
                #  2,3,5,4,1 
                # 2>1 
                # 1,3,5,4,2
#                

# After each Iteration minimum value swap into first position
# 1st iteration - 1
# 2st iteration - 2
# 3st iteration - 3
# 4st iteration - 2
# 5st iteration - 5
 
