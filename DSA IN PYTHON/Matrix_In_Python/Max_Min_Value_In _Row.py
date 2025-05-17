m=[[1,2,3],
   [4,10,6],
   [7,8,9]]

for i in range(len(m)):
    max=0
    for j in range(len(m[i])):
        if m[i][j]>max:
            max=m[i][j]
    print(max,end="\n")
    

print("Minimum Value")

m=[[1,2,3],
   [4,-1,6],
   [7,8,2]]

for i in range(len(m)):
    min=m[i][0]
    for j in range(len(m[i])):
        if m[i][j]<min:
            min=m[i][j]
    print(min,end="\n")
    