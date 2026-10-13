

   # removing duplicate data from a list ?

num = [1,2,2,3,3,3,4,4,5]

unique = set(num)   # use of constructor method set()
print(f"after removing duplicates : {unique}")

   # finding common students in two classes ?

class1 = {"ravi","asha","neha"}
class2 = {"asha","rahul","neha"}

print(class1 & class2)  # use of intersection

data = {1,2,3,"red","drag",5,9,6}
print(f"the set is : {data}")

for i in data:
    print(f"accessing each element through loop in set -> {i}")
