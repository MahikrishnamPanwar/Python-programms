
f = open("text.txt","w")
f.write("hello world \n")
f.write("what a beautiful day it is")
f.close()

f = open("text.txt","r")
print(f.read())
f.close()
