       # nested dictionaries

employee = {"emp1":{"name":"john","salary":50000,"dept":"HR"},"emp2":{"name":"Sara","salary":60000,"dept":"IT"},"emp3":{"name":"Karan","salary":90000,"dept":"finance"}}

# for i,j in employee.items():
#     print(f"{i}->{j}")

print(employee["emp2"]["dept"])
print(employee["emp1"])
print(employee["emp3"]["salary"])
print(employee["emp2"]["name"])
print(f"employee name -> {employee['emp3']['name']}\nemployee salary -> {employee['emp3']['salary']}\nemployee dept -> {employee['emp3']['dept']}")

print(f"the count of items -> {len("emp1")}")

employee["emp3"].update({"salary":150000,"dept":"marketing"})
print(f"the updated data of emp3 -> {employee['emp3']}")

employee.update({'emp4':{"name":"abhi","salary":85000,"dept":"tech"}})
print(f"after adding new data of emp4 the dict is -> {employee}")

data = employee.pop("emp2")
print(f"the pop data of employee -> {data}")


orders = {'ord1':{'product':'phone','price':50000,'status':'delivered'},'ord2':{'product':'sneakers','price':25000,'status':'shipped'},'ord3':{'product':'watch','price':15000,'status':'pending'}}

print(f"the data of orders is -> {orders}")
print(f"the status of ord3 -> {orders['ord3']['status']}")
print(f"the price of ord1 -> {orders['ord1']['price']}")
print(f"the product of ord2 -> {orders['ord2']['product']}")
print(f"the detail of ord1 -> {orders['ord1']} \n product of ord1 is : {orders['ord1']['product']} \n price of ord1 is : {orders['ord1']['price']} \n status of ord1 is : {orders['ord1']['status']} ")

orders['ord2'].update({'status':'delivered'})
orders['ord3'].update({'status':'shipped'})
print(f"the detail after update of ord2 -> {orders['ord2']}\nthe detail after update of ord3 -> {orders['ord3']}")

detail = orders.pop('ord1')
print(f"the detail of ord1 after pop -> {detail}")

# for a,b in orders.items():
#     print(f"{a} -> {b}")
