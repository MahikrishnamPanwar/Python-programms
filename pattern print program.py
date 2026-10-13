#programs

n = int(input("enter the number of rows: "))
k = 1
for i in range(n):
    for j in range(1,i+2):
        print('$',end="")
    print()

n = int(input("enter the number of rows: "))
k = 1
for i in range(n):
     for j in range(1, i + 2):
         print(i+1, end="")
     print()

n = int(input("enter the number of rows: "))
k = 1
for i in range(n):
    for j in range(1,i+2):
        print(k,end="")
        k+=1
    print()


