import math

# 1

degree = 15

radian = degree * (math.pi / 180)

print("Output radian:", round(radian, 6))


# 2

height = 5
base1 = 5
base2 = 6

area = (base1 + base2) * height / 2

print("Expected Output:", area)


# 3

sides = 4
length = 25

polygon_area = (sides * length ** 2) / (4 * math.tan(math.pi / sides))

print("The area of the polygon is:", int(polygon_area))


# 4

base = 5
height = 6

parallelogram_area = base * height

print("Expected Output:", float(parallelogram_area))