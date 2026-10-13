balance = 5000
print("starting balance:", balance)

balance += 10000
balance -= 2000
balance *= 2
balance //= 500

print("final balance:",balance)

num = int(input("enter a number: "))

num += 20
print("after adding 20:",num)

num *= 3
print("after multiplying by 3:",num)

num /= 5
print("after dividing by 5:",num)

num -= 6
print("after subtracting by 6:",num)

num %= 8
print("after modulus by 8:",num)

num **= 4
print("after power by 4:",num)

num = float(input("enter a number:"))
num -= num * 20/100
print("number after reducing 20%:",num)