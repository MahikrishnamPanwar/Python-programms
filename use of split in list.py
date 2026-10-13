       # Use of split in list (taking user input separated by space or any symbol)

# a = input("enter a number space separated :").split()
# nums = []
#
# for x in a:
#     nums.append(int(x))
#
# print(nums)
#    # checking even numbers in list created by user input
# for i in nums:
#     if i % 2 == 0:
#         print("even no. in list created by user input is :",i)
#    # checking odd numbers in list created by user input
# for i in nums:
#     if i % 2 != 0:      # or if i % 2 - 1 == 0:
#         print("odd no. in list created by user input is :",i)

     # write a program which separates the both even and odd numbers into two diff. Lists ?

# b = input("enter a number coma separated :").split(",")
# nums = []
# even = []
# odd = []
#
# for i in b:
#     nums.append(int(i))
# print("the list is :",nums)
#
# for y in nums:
#     if y % 2 == 0:
#         even.append(y)
#     else:
#         odd.append(y)
#
# print("even numbers are :",even)
# print("odd numbers are :",odd)

    # write a program that removes duplicates from list ?

l = [1, 2, 3, 4, 4, "apple", 5, 6, "apple", 4.5, 4.5, 7, 9, 8, 9, 88, 10, 11]
x = []

for i in l:
    if i not in x:
        x.append(i)
print("the list after removing duplicates :", x)

    # write a program that merges two lists ?

# data = [2, 5.56, 3.14, 56]
# data_num = [88, 99, 7, 100]
# b = data + data_num
# x = []
#
# x.extend(b)
# x.sort()
# print("list after merging two lists :", x)

         # merging two list created by user input

# l1 = input("enter the first list :").split(",")
# l2 = input("enter the second list :").split(",")
#
# l = l1 + l2
# print("the list after merging :", l)
