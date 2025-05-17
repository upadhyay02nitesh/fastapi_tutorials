m = [[0,0,1],
    [0,0,0,0],
    [0,0,1,1]]
l=[]

for i in range(len(m)):
    count=0
    for j in range(len(m[i])):
        if m[i][j]==0:
            count+=1
    l.append(count)
max=0
for i in range(len(l)):
    if l[i]>max:
        max=l[i]

for i in range(len(l)):
    if max==l[i]:
        print("Highest Zero In Index Of ",i ," Zero Is=",max)
        break


    

