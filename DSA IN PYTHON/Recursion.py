#Function call itself again and again

# Sum of natural number

# 1. Base approach

# def base_sum(n):
#     s=0
#     i=1
#     while i<n+1:
#         s=s+i 
#         i+=1 
#     return s 
# print(base_sum(5))

# # 2. Recursive approach

# def recursive_sum(n):
#     if n==1:
#         return 1 
#     else:
#         return n+recursive_sum(n-1)
# print(recursive_sum(5))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# if f(n) problem are there then n + f(n-1) is equally f(n) problem 

# if 5! = 5 * 4!
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ***********************Print n natural number in reverse manner**************

# simple approach

# def rev(n):
#     for i in range(n,0,-1):
#         print(i,end=" ")
# rev(4)

#Recursion approach 
# def recur_rev(n):
#     if n>0:
#         print(n,end=" ")
#         recur_rev(n-1)
        
# recur_rev(5)
        

# ***********************    Print n natural number   ******************
# def recur_num(n):
#     if n>0:
#         recur_num(n-1)
#         print(n,end=" ")
# recur_num(10)


# ***********************    Print n odd natural number   ******************
# def recur_num(n):
#     if n>0:
#         recur_num(n-1)
#         print(2*n-1,end=" ")
# recur_num(10)

# ***********************    Print n even natural number   ******************
# def recur_num(n):
#     if n>0:
#         recur_num(n-1)
#         print(2*n,end=" ")
# recur_num(10)
# ***********************    Print n even natural number reverse manner   ******************
# def recur_num(n):
#     if n>0:
#         print(2*n,end=" ")
#         recur_num(n-1)
# recur_num(10)


# *************************Sum of n natural number *********************


# def recur_sum(n):
#     if n==1:
#         return 1 
#     else:
#         return n+recur_sum(n-1)
# r=recur_sum(10)
# print(r)
# *************************Sum of n natural odd number *********************


# def recur_sum(n):
#     if n==1:
#         return 1 
#     else:
#         return (2*n-1)+recur_sum(n-1)
# r=recur_sum(10)
# print(r)


# *************************Sum of n natural even number *********************


# def recur_sum(n):
#     if n==1:
#         return 2
#     else:
#         return (2*n)+recur_sum(n-1)
# r=recur_sum(10)
# print(r)

# *************************Sum of n factorial number *********************


# def recur_sum(n):
#     if n==1:
#         return 1
#     else:
#         return (n)*recur_sum(n-1)
# r=recur_sum(5)
# print(r)

# *************************Sum of n natural square number *********************


# def recur_sum(n):
#     if n==1:
#         return 1
#     else:
#         return (n**2)+recur_sum(n-1)
# r=recur_sum(5)
# print(r)

# ***********************    Print n fibo number   ******************

# def fibo(n):
#     if n==0:
#         return 0 
#     elif n==1 or n==2:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)
# for i in range(5):
#     print(fibo(i),end=" ")


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# a=0
# b=1
# for i in range(5):
#     print(a,end=" ")
#     temp=a 
#     a=b 
#     b=temp+b

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
