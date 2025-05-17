m=[1,2,3,4,5,6,7,8]
n=[1,2,3,4]
count=0
l=len(n)
for i in n:
    if i in m:
        count+=1
if(count==l):
    print("n is subset of m")
else:
    print("Not Subset")