l=[[1,2,7],
   [4,5,6],
   [7,8,9]]

s=0
m=0
for i in range(len(l)):
    
    for j in range(len(l[i])):
        if i==j:
            s+=l[i][j]
        if(i+j)==len(l)-1:
            m+=l[i][j]
print("Primary   Diagonal :",s)
print("Secondary Diagonal :",m)

