#  # STRING Operators
#
# name = input("enter your name :")
# result = "hi"+' '+'there'
# print(result)
# str1 = 'hello'
# str2 = str1+' '+ name
# print(str2)
#
# # num = int(input("enter a number :"))
# # if num % 2 == 0:
# #     print("even number :",num)
# # else:
# #     print("odd number :",num)
#
# name = input("enter your name :")
# num = int(input("enter a number :"))
#
# result = name*num
# print(result)
#
# name = "abhi"
# if 'a' in name:
#     print("yeh")
# else:
#     print("nah")

  # CREATE A PROGRAM WHICH TAKES USERS INPUT AND DETERMINE THE NO. OF EACH CHARACTERS COUNT ?

# name = input("enter your first string :")
# name1 = input("enter your second string :")
# name2 = input("enter your third string :")
#
# print("your name is :",name+" "+name1+" "+name2)
# print("total number of characters :",len(name+name1+name2))
#
# a = name+name1+name2
#
# for i in name+name1+name2:
#     print("number of each char appear in full_string :",a.count(i))

 # PROGRAM TO DETERMINE THE NUMBER OF EACH CHARACTER GIVEN BY USER INPUT PRESENT IN (ABC$123)

k = input("enter a string :")
k = k.lower()        # To make upper case into lower case

abc123 = "abcdefghijklmnopqrstuvwxyz&*%$#@0123456789"

for j in abc123:
    count = 0
    for i in k:
        if j == i:
            count += 1
    if count != 0:
        print( j +" char-appears "+ str(count)+" times ")

