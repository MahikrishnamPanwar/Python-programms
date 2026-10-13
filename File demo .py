
file = open("demo.txt","r")
print(file.read())
print(file.name)
print(file.mode)

file.close()
print(file.closed)


f = open("demo.txt","r")
print(f.readlines())
f.close()

