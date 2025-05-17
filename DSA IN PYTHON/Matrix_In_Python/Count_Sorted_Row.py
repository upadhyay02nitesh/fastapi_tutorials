m=[[9,8,7],
   [6,5,4],
   [3,2,1],
   [0,1,2],
   [11,22,33]]
s=0
for i in range(len(m)):
    min=m[i][0]
    count=0
    for j in range(len(m[i])):
        if m[i][j]<min:
            count+=1

    if count==0:
        print(m[i])
        s+=1
print("Sorted Row Num Is ::",s)


