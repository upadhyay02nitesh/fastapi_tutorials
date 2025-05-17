m=[[9,8,7],
   [6,5,4],
   [3,2,1],
   [0,1,2]]
 #output = 9 8 7 4 5 6 3 2 1 2 1 0 

for i in range(len(m)):
    if i%2!=0:
            m[i]=m[i][::-1]
    for j in range(len(m[i])):
          print(m[i][j],end=" ")
        