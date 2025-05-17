m=int(input("Enter Number Of Number Of Rows --"))
n=int(input("Enter Number Of Number Of Column --"))
mat=[]
for i in range(m):
    row=[]
    for j in range(n):
        row.append(int(input("EnterThe Element --:")))
    mat.append(row)

print("Sum Of All Element --->")

sum=0
for i in range(len(mat)):
    for j in range(len(mat[i])):
        sum+=mat[i][j]
print(sum)


print("Interchange First And Last  Element --->")

n=len(mat)  #for Row
d=len(mat[0]) #for Column
mat[0][0],mat[n-1][d-1]=mat[n-1][d-1],mat[0][0]
print(mat)



print("Transpose Matrix - Row to Column and Column to Row --->")

s=[]
for i in range(len(mat[0])):
    s.append([0]*len(mat))
for i in range(len(mat)):
    for j in range(len(mat[i])):
        s[j][i]=mat[i][j]
print(s)


# print("90 degree Clock-Wise---> Reverse the Matrix+Transpose ")

# mat=mat[::-1]
 
# s=[]
# for i in range(len(mat[0])):
#     s.append([0]*len(mat))
# for i in range(len(mat)):
#     for j in range(len(mat[i])):
#         s[j][i]=mat[i][j]
# print(s)

print("90 degree Anti-Clock-Wise---> Reverse The element Inside the Matrix+Transpose ")

for i in range(len(mat)):
    mat[i]=mat[i][::-1]

print(mat)
s=[]
for i in range(len(mat[0])):
    s.append([0]*len(mat))
for i in range(len(mat)):
    for j in range(len(mat[i])):
        s[j][i]=mat[i][j]
print(s)