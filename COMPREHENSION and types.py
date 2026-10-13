          #  COMPREHENSION

     # List comprehension

squares = [x**2 for x in range(1,11)]
print(squares)

even = [x**2 for x in range(1,26) if x % 2 == 0]
print(even)

odd = [x**2 for x in range(1,36) if x % 2 != 0]
print(odd)

matrix = [[1,2,3],[4,5,6],[7,8,9]]          # Nested list comprehension
flat = [j for i in matrix for j in i]      # This flattens a 2d list into a 1d list
print(flat)

word = "Dhvani Vaghela"
vowels = [ch for ch in word if ch in 'aeiou']
print(vowels)

       # Dictionary comprehension

squares1 = {x : x**2 for x in range(1,9)}
print(squares1)

data = {'a':10,'b':25,'c':33}
swapped = {k:v for v,k in data.items()}
print(swapped)

marks = {'Abhijeet':85,'Dhvani':70,'dev':35,'omi':75}
passed = {k:v for k,v in marks.items() if v >= 40}
print(passed)

     # Set comprehension

num1 = [1,1,3,3,2,4,5,5,6,6]
unique_squares = {n**2 for n in num1}
print(unique_squares)

    #  Generator comprehension

gen = (x**2 for x in range(1,5))
print(gen)

for n in gen:
    print(n)

data1 = (x for x in range(1,11) if x % 2 == 0)
print(data1)

for i in data1:
    print(i)

gen1 = (x*2 for x in range(1,11) if x % 2 != 0)
print(gen1)

for j in gen1:
    print(j)

      # Nested comprehension (Advanced)

matrix1 = [[5,6,8],[2,9,4],[3,1,7]]
transposed = [[row[i] for row in matrix1]for i in range(3)]   # Transpose means converting rows into columns
print(transposed)

