
try:
    num = int(input("please enter a number: "))
    result = 10 / num

except ZeroDivisionError:
    print("cannot divide by zero")

except ValueError:
    print("please enter a valid number")

else:
    print(f"Division successful : result = {result}")

finally:
    print("program ended")

