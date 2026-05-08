names = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 95]

for index, name in enumerate(names):
    print(index, name)

for name, score in zip(names, scores):
    print(name, score)

numbers = [5, 2, 8, 1]

print(sorted(numbers))

num = "100"

print(int(num))
print(float(num))
print(str(50))

print(type(num))
print(type(100))