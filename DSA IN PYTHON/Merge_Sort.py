def Merge_sort(l):
    if len(l)>1:
        mid=len(l)//2
        left=l[:mid]
        right=l[mid:]
        Merge_sort(left)
        Merge_sort(right)

        i=j=k=0
        while i<len(left) and j<len(right):
            if(left[i]<right[j]):
                l[k]=left[i]
                i+=1
            else:
                l[k]=right[j]
                j+=1 
            k+=1 
        
        while i<len(left):
                l[k]=left[i]
                i+=1
                k+=1

        while j<len(right):
                l[k]=right[j]
                j+=1
                k+=1
    return l 
l=[3,2,1,6,5]
print(Merge_sort(l))

            