
age = int(input("please enter your age: "))

if age < 18 :
    raise ValueError("age must be 18 or above")

else:
    print(f"You are {age} years old\nAccess Granted")

