file = open("sample.txt", "r")

print(file.read())

file.close()

file = open("sample.txt", "r")

print(file.readline())
print(file.readlines())

file.close()

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)