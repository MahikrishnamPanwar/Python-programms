
user = input("enter text to append it :").split(",")

file = open("profile.txt","a")

for word in user:
    file.write(word + "\n")

file.close()

print("details have appended successfully")

with open("profile.txt","r") as file:
    data = file.read()
    print(data)

