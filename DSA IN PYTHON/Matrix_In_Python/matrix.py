m=int(input("Enter Number Of Number Of Rows --"))
n=int(input("Enter Number Of Number Of Column --"))
mat=[]
for i in range(m):
    row=[]
    for j in range(n):
        row.append(int(input("EnterThe Element --:")))
    mat.append(row)
print(mat)
print()
for i in range(len(mat)):
    for j in range(len(mat[i])):
        print(mat[i][j],end=" ")
    print()


# m=3
# n=2

# i=0         row=[]  j=0,1      mat=[]
#             row=[0,1]          mat=[[0,1]]

# i=1        row=[]  j=0,1      mat=[[0,1]]
#             row=[0,1]          mat=[[0,1],[0,1]]

# i=2         row=[]  j=0,1      mat=[[0,1],[0,1]]
#             row=[0,1]          mat=[[0,1],[0,1],[0,1]]
        

