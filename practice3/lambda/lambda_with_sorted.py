students = [
    ("Ali", 85),
    ("Sara", 92),
    ("Tom", 78)
]

sorted_students = sorted(students, key=lambda x: x[1])

print(sorted_students)