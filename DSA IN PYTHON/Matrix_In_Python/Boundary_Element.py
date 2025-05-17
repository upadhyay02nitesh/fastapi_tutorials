m=[[1,2,3],
   [4,5,6],
   [7,8,9]]
for i in range(len(m)):
    for j in range(len(m[i])):
        if (i==0 or i==len(m)-1 ):
            print(m[i][j],end=" ")
        elif j==0 or j==len(m[i])-1:
            print(m[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()