def linear(arr,k):
    for i in range(len(arr)):
        if(arr[i]==k):
            return i
    return False
arr=[19,27,678,89,56]
k=27
f=linear(arr,k)
if(f==False):
    print("Not find")
else:
    print(k,"Find in the index of",f)
    