# for loop and check even or odd through a program
rows = 5
for i in range(1,rows+1):
   for j in range(i):
       print("x",end="")
   print()



def is_odd_or_even(number):
    if number % 2==0:
       return "even"
    else:
       return "odd"
print(is_odd_or_even(56423))
print(is_odd_or_even(36362))

num =int(input("enter a number"))

if num % 2==0:
    print("it is even")
else:
    print("it is odd")

def check_even_odd(n):
    if n % 2 == 0:
       return "even"
    else:
        return "odd"

number  = int(input("enter a number: "))
result = check_even_odd(number)
print("the number is :",result)

num = int(input("enter a number: "))

result = "even" if num % 2==0 else "odd"

print("the number is ",result)
