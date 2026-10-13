# PRACTICE CODE

# n = int(input("enter number of rows :"))
# k = 6
# for i in range(1,n+1):
#     for j in range(1,n+2):
#         if j>1:
#             print("@",end=" ")
#         print(k,end=" ")
#     print()
#
# n = int(input("enter no. of rows :"))
# k = int(input("enter no. of columns :"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("$",end=" ")
#         if j>1:
#             print("@",end=" ")
#         print(k,end=" ")
#     print()

n= int(input("enter no. of rows :"))
k =1
for i in range(n):
    for j in range(1,i+2):
        print("*",end="")
    print()
for i in range(n):
    for j in range(1,i+3):
        print(i+1,end="")
    print()
for i in range(n):
    for j in range(1,i+3):
        print(k,end="")
        k+=1
    print()

