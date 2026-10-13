# define which number is greater through program ?

num1 = int(input("enter the first number :"))
num2 = int(input("enter the second number :"))
num3 = int(input("enter the thrid number :"))

if num1 > num2 and num1 > num3:
    print("num1 is greater :",num1)

elif num2 > num3 and num2 > num1:
    print("num2 is greater :",num2)

elif num3 > num1 and num3 > num2:
    print("num3 is greater :",num3)

else:
    if num1 == num2 == num3:
        print("all are equal")

# shorter form of upper code or pro level coding

num1, num2, num3 = map(int,input("enter three number :").split())

if num1 == num2 == num3:
    print("all are equal")
else:
    print("greatest number :",max(num1, num2, num3))

