class Student:
    school = "KBTU"

    def __init__(self, name):
        self.name = name

student1 = Student("Ali")
student2 = Student("Sara")

print(student1.school)
print(student2.school)

student1.name = "Tom"

print(student1.name)