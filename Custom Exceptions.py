
class InvalidAgeError(Exception):
    pass

try:
    age = int(input("please enter your age: "))
    if age < 18 :
        raise InvalidAgeError
    else:
        print("Eligible to vote!")

except InvalidAgeError:
    print("you must be 18 or above to vote")

