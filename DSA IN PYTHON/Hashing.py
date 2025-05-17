

def Has_function(key):
    return key%10

def insert(Hashtable,key,value):
    has_key=Has_function(key)
    Hashtable[has_key].append(value)

def display(Hashtable):
    for i in range(len(Hashtable)):
        print(i,end=" ")
        for j in Hashtable[i]:
            print("-->",end=" ")
            print(j,end=" ")
        print()
    print()
    # print(Hashtable)

def search(key):
    for i in range(len(Hashtable)):
        for j in Hashtable[i]:
            if j==key:
                return i
    return False
# 
Hashtable=[[] for i in range(10)]
insert(Hashtable,10,'kalu')
insert(Hashtable,25,'shankhu')
insert(Hashtable,20,'pinja')
insert(Hashtable,9,'chinki')
insert(Hashtable,21,'minki')
insert(Hashtable,21,'pinki')
display(Hashtable)
print(search('shankhu'))
# print(Hashtable)
