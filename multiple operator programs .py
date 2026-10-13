a = 50
b = 5
sum_ab = a+b
product = a*b

sum_ab += 10

is_greater = sum_ab>product
is_equal = a==b

logical_result = is_greater or not  is_equal

numbers = [10,30,40]
check_membership = a in numbers

x = a
identity_check = x is not a

print("sum after assignment:",sum_ab)
print("product :",product)
print("is sum_ab greater than product?",is_greater)
print("are a and b equal?",is_equal)
print("logical result:", logical_result)
print("is a in numbers list?",check_membership)
print("do x and a refer to same object?", identity_check)

