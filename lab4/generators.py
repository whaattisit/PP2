# Task 1

print("Task 1: \n")
def square(): 
    n = int(input("Your number: "))
    for i in range(1, n):
        yield i ** 2

gen = square()
for numb in gen:
    print(numb)

# Task 2

print("\nTask 2: \n")
def even(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Your number: "))
gen = even(n)
for i in range(int(n/2)):
    print(next(gen), end=", ")
print(next(gen))

# Task 3

print("\nTask 3: \n")
def twelve(n):
    for i in range(n + 1):
        if (i % 12 == 0):
            yield i
n = int(input("So what is your number: "))
gen = twelve(n)
for numb in gen:
    print(numb)

# Task 4

print("\nTask 4: \n")
def squares(a, b):
    for i in range (a, b + 1):
        yield i ** 2
a = int(input("Now two numbers please: "))
b = int(input())
gen = squares(a, b)
for numb in gen:
    print(numb)

# Task 5

print("\nTask 5: \n")
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
n = input("And the last number: ")
gen = countdown(n)
for numb in gen:
    print(numb)