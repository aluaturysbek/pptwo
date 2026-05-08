# 1

def squares_generator(n):
    for i in range(n + 1):
        yield i * i

for value in squares_generator(5):
    print(value)


# 2

n = int(input("Enter number: "))

even_numbers = (str(i) for i in range(n + 1) if i % 2 == 0)

print(",".join(even_numbers))


# 3

def divisible(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for value in divisible(50):
    print(value)


# 4

def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

for value in squares(1, 5):
    print(value)


# 5

def countdown(n):
    while n >= 0:
        yield n
        n -= 1

for value in countdown(10):
    print(value)