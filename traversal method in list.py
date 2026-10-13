                 # TRAVERSAL METHOD IN LIST

  # create a list and determine the elements on the even and odd position ?

num = [1,56,88,2,25,33,99,46,50,77]
  # checks even position in list (num)
for i in range(len(num)):
    if i % 2 == 0 :
      print(num[i])

name = ["bhopal","indore","baroda","gwalior","ratlam","agra"]
  # checks odd position in list (name)
for i in range(len(name)):
    if i % 2 - 1 == 0 :
        print(name[i])

# check each element in matrix for nested list

matrix = [[11,22,33],[44,55,66],[77,88,99]]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j])

    # visiting each element in list (fruits) using while and for loop (Traversal)

fruits = ["kiwi","apple","banana","orange","grapes"]
i = 0
   # using while loop
while i < len(fruits):
    print(fruits[i])
    i+=1
   # using for loop
for i in range(len(fruits)):
    print(fruits[i])

    # take user input and append the list

x = int(input("enter a number :"))
l = []

for i in range(x):
    item = input("enter item :")
    i = i + 1
    l.append(item)
print("your list is :",l)

   # sum and average of numbers in list

num = [5,10,25,18,7,66]
sum = 0

for i in range(0,len(num)):
     sum = sum + num[i]
print("the total sum of the list is :",sum)
print("average of list is :",sum/len(num))

  # take user input to check that city is present or not in the list

city = ["indore","gwalior","agra","bhopal","ratlam","ujjain","delhi","mumbai","kolkata"]

n = input("enter the city name :")

if n in city:
    print(n, "-- is present in the list :" ,city)
    # print(f"{n} is present in :",city)
else:
    print(n, "-- not found in the list :" ,city)
    # print(f"{n} not found in :",city)

