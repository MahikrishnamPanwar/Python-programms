# scope program

# x = "global"  # global scope

#def outer_function():
 #   x="enclosing"  # enclosing scope

  #  def inner_function():
   #     x="local"  # local scope
    #    print("inside inner_function(local):",x)

  #  inner_function()
   # print("inside outer_function(enclosing):",x)

#outer_function()
#print("outside all function (global):",x)


num1 =1

def demo():
    num2 =2
    print("variable inside demo function:",num2)
    print("variable outside method:",num1)
    def demo2():
        num3 =5
        print(num2)
    #print(num3)    #this will give error

demo()
print("variable outside demo function:",num1)
#print("variable j is :",num2)   #this will give error


