# LIST PROGRAMS

# L1 = []
# L2 = [5,9,8,2]
# L3 = [1,"Abhijeet",True,3.5]
# L4 = [[6,7],[3,4],['omi',False]]
# L5 = [[8,9],'abc',4.2,True,['abc','xyz']]
#
# print(L5[1:4])
# print(L3[1])

x = [10,25,38,49,55,67,72,84]
y = ["apple","kiwi","pomegranate","blue cherry","banana","fig","grape"]
z = [200,"python",3.14,True,"code",95,False]
 #  Using INDEXING
# print("the first element is :",x[0])
# print("the last element is :",x[-1])
# print("the fourth element is :",y[3])
# print("access fig using index :",y[5])
# print("second last in z is :",z[-2])
# print("boolean value in z is :",z[3])
#  # Using SLICING
# print("the first 3 element in x are :",x[0:3])
# print("slicing element from 2-5 in x :",x[2:6])
# print("every second element from x :",x[::2])
# print("reverse list x :",x[::-1])
# print("extract are :",y[1:4])
# print("last 3 element in y are :",y[4:])
# print("reverse list y is :",y[::-1])
# print("slice only string elements from z :",z[1::3])
#  # Using MUTABILITY
# x[0] = 999
# print("changing 1st element in x :",x)
# y[3] = "mango"
# print("replacing blue cherry with mango :",y)
# z[2] = 6.28
# print("changing 3.14 in z :",z)
# y.append("orange")
# print("adding new element in y :",y)
# z.insert(0,"start")
# print("inserting start in z :",z)
# y.remove("banana")
# print("removing banana in y :",y)
# del x[-1]
# print("deleting last element in x :",x)
# x[2:5] = [0,0,0]
# print("replacing it with 0 in x :",x)
#  # programing on list with multiple list in it
#
main_list = [[10,20,30],["apple","banana","cherry"],[1.1,2.3,4.6]]
#
# print(main_list[1][-2])
# print(main_list[-1][2])
# print(main_list[2][1:])
# print(main_list[1][::-1])
#
# main_list[-1][1] = 9.9
# print(main_list)
# main_list[1].append("kiwi")
# print(main_list)

# x.sort()
# y.sort()
# print(x,y)
#
# main_list.reverse()
# print(main_list)
#
# main_list.insert(1,[True,False])
# print(main_list)
#
# popped = main_list.pop(1)
# print(main_list)
# print("removed :",popped)
#
# z.remove("python")
# print(z)
#
# num = [1,2,3,4,5]
# full_list = num + x + y + main_list + z
# print(full_list)
# print(num*3)
# print(len(full_list))
#
# y.append(x+z)
# print(y)
#
# z.insert(2,"python")
# print(z)
#
# full_list.reverse()
# print(full_list)
# print(full_list[::-1])
#
# print(full_list[0:30:4])
# print(full_list[2:5])
# print(full_list[7][1])
# print(full_list[14])
# print(full_list[15:25])
# print(full_list[0::7])

z.extend(["python",3.14])
print(z)
print(z.index('code'))
print(z.count(3.14))
w = z.copy()
print(w)
w.clear()
print(w)


l = [5,6,2,4,9,7]
print(l)
print(len(l))
print(max(l))
print(min(l))
print(sum(l))
print(sorted(l))
