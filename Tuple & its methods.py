     # TUPLE

nums = (10,20,30,40,50,60,60,60,70)

print("type of nums :",type(nums))
print("number of elements :",len(nums))
print("second element :",nums[2])
print("last element :",nums[-1])
print("multiple elements :",nums[1:5])
print("index of 40 :",nums.index(40))
print("count of 60 :",nums.count(60))

   # Tuple packing

t = (25,36,55,"naruto")
print("packed tuple",t)

   # Tuple unpacking

t1 = (999,666,333)
x,y,z = t1
print("x :",x)
print("y :",y)
print("z :",z)

t = (1,(4,5),(10,11,12))
print(t[1])
print(t[1][1])

    # nested tuple and unpacking it

t = (1,2,(3,4,(5,6)),7)
print(t[2][2][0])
print(t[2])
a,b,(c,d,(e,f)),g = t
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
