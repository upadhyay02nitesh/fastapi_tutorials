m=[[1,2,3],
   [4,5,6],
   [7,8,9]]
n=[[11,22,33,0],
   [44,55,66,0],
   [77,88,99,0]]

#order m=3*3 and n=3*4 then p order ===row of m and column of n =3*4

# 1 2 3 
#         11
#         44
#         77

# 1*11+2*44+3*77=p[0]=330

p=[]
for i in range(len(m)):
    p.append([0]*len(n[0]))

for i in range(len(m)):
    for j in range(len(n[0])):
        for k in range(len(n)):
            p[i][j]+=m[i][k]*n[k][j]
print(p)