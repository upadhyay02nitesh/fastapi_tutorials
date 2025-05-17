m=[[9,8,7],
   [6,5,4],
   [3,2,1]]
s=[]
for i in range(len(m)):
    for j in range(len(m[i])):
        s.append(m[i][j])
for i in range(1,len(s)):
    j=i-1
    temp=s[i]
    while j>=0 and temp<s[j]:
        s[j+1]=s[j]
        j-=1
    s[j+1]=temp
for i in range(0,len(s)):
        if i%3==0:
             print("\n")
        print(s[i],end=" ")

    
