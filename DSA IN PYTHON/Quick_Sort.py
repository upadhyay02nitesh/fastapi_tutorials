def Quick_Sort(l):
    if len(l)<=1:
        return l
    else:
        pivot=l.pop()
        lower=[]
        greater=[]
        for i in l:
            if i>pivot:
                greater.append(i)
            else:
                lower.append(i)
        return Quick_Sort(lower)+[pivot]+Quick_Sort(greater)

        

l=[3,4,6,2,6,8,2,5]
print(Quick_Sort(l))

[3,4,6,2,6,8,2,5]
pivot=5 

# lower                       pivot                       higher
# 3,2,2,4                     5                           6,6,8

# pivot=4                                                 pivot=8

# 2,2,3  4                  5                             6,6  8
# pivot=3                                                 pivot=6
# 2,2  3  4                 5                             6 6 8
# pivot=2
# 2 2 3 4                   5                             6 6 8


#             [2,2,3,4,5,6,6,8 ]                    

