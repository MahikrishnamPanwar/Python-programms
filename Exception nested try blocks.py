
try:
    try:
        num = int(input("enter a number :"))
        result = 10 / num
        print(f"the result is : {result}")

    except ZeroDivisionError:
        print("can't divide by zero")

except ValueError:
    print("enter a valid number")
