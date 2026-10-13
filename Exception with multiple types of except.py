
try:
    num = int(input("Enter a number: "))
    result = 50 / num
    print(f"result is : {result}")

except ZeroDivisionError:
    print("cannot divide by zero")

except ValueError:
    print("please enter a valid number")
