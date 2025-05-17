m=[[1,2,3],
   [4,5,6],
   [7,8,9]]
n=[[11,22,33],
   [44,55,66],
   [77,88,99]]

p=[]
for i in range(len(m)):
    p.append([0]*len(m[0]))

if (len(m)==len(n) and len(m[0])==len(n[0])):
    for i in range(len(m)):
        for j in range(len(m[0])):
            p[i][j]=m[i][j]+n[i][j]
    print(p)
            

else:
    print("Sum is not Possible Matrix is not in same order!!!")
