 # calculator programme using nesting if,elif,else:

print("enter 1 for add")
print("enter 2 for subtract")
print("enter 3 for division")
print("enter 4 for multiply")

choice = int(input("enter your choice:"))

num1 = float(input("enter the first number:"))
num2 = float(input("enter the second number:"))

if choice == 1:
    result = num1 + num2
    print("addition =",result)

elif choice == 2:
       result = num1 - num2
       print("subtraction =",result)

elif choice == 3:
      if num2 !=0:
         result = num1 / num2
         print("division =",result)
      else:
         print("division by zero is not allowed")

elif choice == 4:
      result = num1 * num2
      print("multiplication =",result)

else:
      print("invalid choice")

  #shorter form of code

print("1:add 2:subtract 3:division 4:multiply")

c =int(input("choice:"))
a,b = map(float, input("enter two number: ").split())

if c == 1:
     print("result =",a+b)
elif c == 2:
     print("result =",a-b)
elif c == 3:
     print("result =","not allowed" if b == 0 else a/b)
elif c == 4:
     print("result =",a*b)
else:
     print("invalid choice")

