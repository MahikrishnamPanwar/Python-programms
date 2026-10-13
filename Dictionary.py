        # DICTIONARY

# student = {"name":"dev","age":20,"dob":"1jan1999"}
#
# print(student)
# print(student["name"])
# print(student.get("age"))
#
# student["address"] = "Bangalore"
# print(student)
#
# student["age"] = 30
# print(student)
# print("length of student :",len(student))
# del student["dob"]
# print(student)
#
# d = student.popitem()
# d1 = student.pop("name")
# print(d)
# print(d1)
#
# student.clear()
# print(student)
# print("length of student after clear :",len(student))

product = {"id": 101,"name":"laptop","price":80000,"stock":20}

print(product.keys())
print(product.values())
print(product.items())
print(product["price"])
print(product.get("Name"))
print(product.get("name"))


     # using loops on dictionaries

dict1 = {"name":"omi","address":"goa","age":20,"dob":"19 dec 2005"}

for i in dict1:
    print(f"{i} : {dict1[i]}")

for key,value in dict1.items():
    print(f"{key} : {value}")

data = {"a": 1, "b": 2}

s = str(data)

print(s)
print(type(s))   # <class 'str'>
