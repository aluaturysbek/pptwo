from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

squared = list(map(lambda x: x ** 2, numbers))
print(squared)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

sum_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_numbers)

print(len(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))