             # SET PROGRAMS

# fruits = {"apple","banana","cherry"}
#
# print(fruits)
# print(type(fruits))
# print(len(fruits))
#
# fruits.add("kiwi")
# print(f"after adding a element :{fruits}")
#
# fruits.update(["angoor","mango"])
# print(f"{fruits} -> after adding multiple elements")
#
# fruits.remove("angoor")
# print(f"after removing angoor -> {fruits}")
#
# fruits.discard("orange")
# print(f"if element doesn't exist in set when use of discard output will be : {fruits} ")
#
# new_fruits = fruits.pop()
# print(new_fruits)



num = {1,2,2,22,3,6,5,5,4,8,9,22}
print(num)


num1 = {1,2,3,4,5,6}
num2 = {4,5,6,7,8,9}

print(f"use of union (A|B) -> {num1|num2}")    # or (num1.union(num2))
print(f"use of intersection (A & B) -> {num1&num2}")
print(f"use of difference (A-B) -> {num1-num2}")
print(f"use of symmetric difference (A^B) -> {num1^num2}")
print(f"{len(num1)} : no. of elements in num1 and {len(num2)} : no. of elements in num2")
print(f"sum of num1 : {sum(num1)} and sum of num2 : {sum(num2)}")


print(num1.issubset(num2))   # True if all elements of A are in B else False
print(num1.issuperset(num2))  # True if A contains all elements of B else False
print(num1.isdisjoint(num2))   # True if A and B have no common elements else False
